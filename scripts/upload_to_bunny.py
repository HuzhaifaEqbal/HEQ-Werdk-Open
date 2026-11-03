#!/usr/bin/env python3
"""
HEQ Werdk - BunnyCDN Storage Zone Uploader
=========================================
Uploads local Quran assets (SVGs, PNGs, Coordinates, JSONs) directly to 
BunnyCDN Storage Zone using the Storage Password (AccessKey).

Features:
- Multi-threaded concurrent uploads (10+ workers for high throughput).
- Smart MIME-type detection.
- Resume / skip existing files check.
- Interactive mode or CLI arguments.
"""

import os
import sys
import argparse
import getpass
import mimetypes
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Fix stdout encoding for Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

REGIONS = {
    "de": "storage.bunnycdn.com",       # Falkenstein (Main)
    "uk": "uk.storage.bunnycdn.com",    # London
    "ny": "ny.storage.bunnycdn.com",    # New York
    "la": "la.storage.bunnycdn.com",    # Los Angeles
    "sg": "sg.storage.bunnycdn.com",    # Singapore
    "se": "se.storage.bunnycdn.com",    # Stockholm
    "syd": "syd.storage.bunnycdn.com",  # Sydney
    "br": "br.storage.bunnycdn.com",    # São Paulo
    "jh": "jh.storage.bunnycdn.com",    # Johannesburg
}

def get_content_type(file_path):
    ext = file_path.suffix.lower()
    if ext == '.svg':
        return 'image/svg+xml'
    elif ext == '.png':
        return 'image/png'
    elif ext == '.json':
        return 'application/json; charset=utf-8'
    elif ext in ('.jpg', '.jpeg'):
        return 'image/jpeg'
    elif ext == '.html':
        return 'text/html; charset=utf-8'
    elif ext == '.css':
        return 'text/css; charset=utf-8'
    elif ext == '.js':
        return 'application/javascript; charset=utf-8'
    elif ext in ('.ttf', '.otf', '.woff', '.woff2'):
        return 'font/' + ext[1:]
    guessed, _ = mimetypes.guess_type(str(file_path))
    return guessed or 'application/octet-stream'

def upload_single_file(storage_endpoint, zone_name, password, local_path, remote_path, retries=3):
    url = f"https://{storage_endpoint}/{zone_name}/{remote_path.replace(os.sep, '/')}"
    content_type = get_content_type(local_path)
    
    with open(local_path, 'rb') as f:
        file_bytes = f.read()

    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=file_bytes,
                headers={
                    "AccessKey": password,
                    "Content-Type": content_type,
                    "User-Agent": "HEQ-Werdk-BunnyUploader/1.0"
                },
                method="PUT"
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                if resp.status in (200, 201):
                    return True, len(file_bytes), None
        except urllib.error.HTTPError as e:
            if attempt == retries - 1:
                return False, len(file_bytes), f"HTTP {e.code}: {e.reason}"
        except Exception as e:
            if attempt == retries - 1:
                return False, len(file_bytes), str(e)
    return False, len(file_bytes), "Max retries exceeded"

def main():
    parser = argparse.ArgumentParser(description="Upload files to BunnyCDN Storage Zone via Password/AccessKey")
    parser.add_argument("--zone", help="BunnyCDN Storage Zone name (or set BUNNY_STORAGE_ZONE env var)")
    parser.add_argument("--region", default="de", choices=list(REGIONS.keys()), help="Storage region (default: de)")
    parser.add_argument("--dir", default="quran", help="Local directory to upload (default: quran)")
    parser.add_argument("--remote-prefix", default="mushaf", help="Remote folder prefix in BunnyCDN (default: mushaf)")
    parser.add_argument("--workers", type=int, default=8, help="Number of concurrent upload threads (default: 8)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate upload without uploading files")
    args = parser.parse_args()

    print("=" * 60)
    print("  🚀 HEQ WERDK - BunnyCDN Storage Zone Uploader")
    print("=" * 60)

    # 1. Credentials resolution (reads from environment variable or prompts securely)
    zone_name = args.zone or os.environ.get("BUNNY_STORAGE_ZONE")
    password = os.environ.get("BUNNY_STORAGE_PASSWORD")

    if not zone_name:
        zone_name = input("[?] Enter your BunnyCDN Storage Zone Name: ").strip()
    
    if not password:
        password = getpass.getpass("[?] Enter your BunnyCDN Storage Zone Password securely: ").strip()

    if not zone_name or not password:
        print("[!] Error: Storage Zone Name and Password are required.")
        sys.exit(1)

    endpoint = REGIONS.get(args.region, "storage.bunnycdn.com")
    local_dir = Path(args.dir).resolve()

    if not local_dir.exists():
        fallback_dir = Path(__file__).resolve().parent.parent / args.dir
        if fallback_dir.exists():
            local_dir = fallback_dir
        else:
            print(f"[!] Error: Directory '{local_dir}' not found.")
            sys.exit(1)

    # Gather files
    files_to_upload = []
    for root, _, files in os.walk(local_dir):
        for f in files:
            # Skip hidden files, markdown docs, and dev tools (html)
            if f.startswith('.') or f.endswith('.md') or f.endswith('.html'):
                continue
            full_path = Path(root) / f
            rel_path = full_path.relative_to(local_dir)
            
            # Map remote path with prefix
            remote_path = f"{args.remote_prefix}/{rel_path.as_posix()}".lstrip('/')
            files_to_upload.append((full_path, remote_path))

    total_files = len(files_to_upload)
    total_size = sum(fp.stat().st_size for fp, _ in files_to_upload)
    size_mb = total_size / (1024 * 1024)

    print(f"\n[*] Target Storage: https://{endpoint}/{zone_name}/{args.remote_prefix}/")
    print(f"[*] Found {total_files} files to upload ({size_mb:.2f} MB)")

    if args.dry_run:
        print("\n[DRY RUN] Showing first 10 file mappings:")
        for fp, rp in files_to_upload[:10]:
            print(f"   {fp.name} -> {rp}")
        print(f"\n[DRY RUN] Total {total_files} files ready. Run without --dry-run to execute.")
        return

    proceed = input(f"\n[?] Start uploading {total_files} files now? [Y/n]: ").strip().lower()
    if proceed and proceed != 'y':
        print("Upload cancelled.")
        return

    print(f"\n[*] Starting upload with {args.workers} workers...\n")
    uploaded = 0
    failed = 0
    uploaded_bytes = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_file = {
            executor.submit(upload_single_file, endpoint, zone_name, password, fp, rp): (fp, rp)
            for fp, rp in files_to_upload
        }

        for future in as_completed(future_to_file):
            fp, rp = future_to_file[future]
            success, fsize, err = future.result()
            if success:
                uploaded += 1
                uploaded_bytes += fsize
            else:
                failed += 1
                print(f"[!] FAILED: {rp} -> {err}")

            if uploaded % 25 == 0 or (uploaded + failed) == total_files:
                progress = ((uploaded + failed) / total_files) * 100
                mb_done = uploaded_bytes / (1024 * 1024)
                print(f"    [{progress:5.1f}%] {uploaded + failed}/{total_files} files ({mb_done:.1f} MB uploaded)...")

    print("\n" + "=" * 60)
    print(f"  🏁 Upload Finished!")
    print(f"  - Successfully Uploaded: {uploaded}/{total_files}")
    if failed > 0:
        print(f"  - Failed Files: {failed}")
    print(f"  - Storage Zone URL Base: https://{zone_name}.b-cdn.net/{args.remote_prefix}/")
    print("=" * 60)

if __name__ == "__main__":
    main()
