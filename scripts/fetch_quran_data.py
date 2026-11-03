"""
HEQ Werdk - Quran Data & Coordinates Fetcher (Hafs & Warsh)
===========================================================
This script downloads, normalizes, and packages authentic Quran data for:
1. Hafs ('Aasim) - مجمع الملك فهد (KFGQPC) / Tanzil
2. Warsh ('An Nafi') - مجمع الملك فهد (KFGQPC)

Outputs:
- JSON Surah files for both Riwayat with Uthmanic & simplified search texts.
- Page Manifests mapping Pages (1-604), Surahs, Juz, and Hizb.
- Ayah polygon coordinates for all 604 pages (for verse tracking / highlighting).
- SVG page artwork (optional or on demand).
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Fix stdout encoding for Windows cp1256
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).resolve().parent.parent
QURAN_DIR = BASE_DIR / "quran"

HAFS_DIR = QURAN_DIR / "hafs"
WARSH_DIR = QURAN_DIR / "warsh"

# Endpoints for authentic King Fahd Complex (KFGQPC) text data
URL_HAFS_DATA = "https://cdn.jsdelivr.net/gh/thetruetruth/quran-data-kfgqpc@master/hafs/data/hafsData_v18.json"
URL_WARSH_DATA = "https://cdn.jsdelivr.net/gh/thetruetruth/quran-data-kfgqpc@master/warsh/data/warshData_v10.json"

# Endpoints for ayah coordinate polygons (604 pages)
URL_COORDS_HAFS = "https://raw.githubusercontent.com/quran-ws/quran-svg/main/mushafs/hafs/kfqc/json/{page:03d}.json"
URL_COORDS_WARSH = "https://raw.githubusercontent.com/quran-ws/quran-svg/main/mushafs/warsh/kfqc/json/{page:03d}.json"

# Endpoints for SVG page vectors (604 pages)
URL_SVG_HAFS = "https://raw.githubusercontent.com/quran-ws/quran-svg/main/mushafs/hafs/kfqc/svg/{page:03d}.svg"
URL_SVG_WARSH = "https://raw.githubusercontent.com/quran-ws/quran-svg/main/mushafs/warsh/kfqc/svg/{page:03d}.svg"

HEADERS = {
    "User-Agent": "HEQ-Werdk-QuranDataSync/1.0 (https://heqwerdk.com)"
}

def fetch_url(url, retries=3, timeout=30):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(1 + attempt)

def parse_page(val):
    """Safely parse page number or range (e.g. '85-86') into start and end."""
    if val is None:
        return 1, 1
    s = str(val).strip()
    if '-' in s:
        parts = s.split('-')
        try:
            return int(parts[0]), int(parts[1])
        except Exception:
            return 1, 1
    try:
        p = int(s)
        return p, p
    except Exception:
        return 1, 1

def clean_arabic_search(text):
    """Normalize Arabic text for searching without diacritics."""
    import re
    # Remove Tashkeel / Harakat
    tashkeel = re.compile(r'[\u0617-\u061A\u064B-\u0652\u0670\u06D6-\u06ED]')
    text = tashkeel.sub('', text)
    # Normalize Alef forms
    text = re.sub(r'[إأآٱ]', 'ا', text)
    # Normalize Teh Marbuta
    text = re.sub(r'ة', 'ه', text)
    # Normalize Ya / Alef Maksura
    text = re.sub(r'ى', 'ي', text)
    # Remove non-letters/numbers
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_texts(riwayah="hafs"):
    print(f"[*] Processing {riwayah.upper()} text data...")
    target_dir = HAFS_DIR if riwayah == "hafs" else WARSH_DIR
    surahs_dir = target_dir / "surahs"
    surahs_dir.mkdir(parents=True, exist_ok=True)

    url = URL_HAFS_DATA if riwayah == "hafs" else URL_WARSH_DATA
    raw_bytes = fetch_url(url)
    raw_data = json.loads(raw_bytes.decode('utf-8'))
    print(f"    Loaded {len(raw_data)} verses for {riwayah}.")

    # Group by surah
    surahs_map = {}
    for item in raw_data:
        s_no = int(item.get('sora') or item.get('sura_no') or 0)
        s_name_ar = str(item.get('sora_name_ar') or item.get('sura_name_ar') or '').strip()
        s_name_en = str(item.get('sora_name_en') or item.get('sura_name_en') or '').strip()
        p_start, p_end = parse_page(item.get('page', 1))

        if s_no not in surahs_map:
            surahs_map[s_no] = {
                "number": s_no,
                "name_ar": s_name_ar,
                "name_en": s_name_en,
                "page_start": p_start,
                "page_end": p_end,
                "ayahs": []
            }
        
        if p_end > surahs_map[s_no]["page_end"]:
            surahs_map[s_no]["page_end"] = p_end

        emlaey = str(item.get('aya_text_emlaey') or '').strip()
        simple_txt = emlaey if emlaey else clean_arabic_search(str(item.get('aya_text', '')))

        ayah_entry = {
            "id": int(item.get('id', 0)),
            "number": int(item.get('aya_no', 0)),
            "text_uthmani": str(item.get('aya_text', '')).strip(),
            "text_simple": simple_txt,
            "juz": int(item.get('jozz', 1)),
            "page": p_start,
            "page_end": p_end if p_end != p_start else None,
            "line_start": int(item.get('line_start') or 1),
            "line_end": int(item.get('line_end') or 1)
        }
        surahs_map[s_no]["ayahs"].append(ayah_entry)

    # Write each surah file and build manifest
    manifest_surahs = []
    for s_no in sorted(surahs_map.keys()):
        surah_data = surahs_map[s_no]
        surah_file = surahs_dir / f"{s_no:03d}.json"
        with open(surah_file, 'w', encoding='utf-8') as f:
            json.dump({
                "number": surah_data["number"],
                "name_ar": surah_data["name_ar"],
                "name_en": surah_data["name_en"],
                "ayahs_count": len(surah_data["ayahs"]),
                "page_start": surah_data["page_start"],
                "page_end": surah_data["page_end"],
                "ayahs": surah_data["ayahs"]
            }, f, ensure_ascii=False, indent=2)

        manifest_surahs.append({
            "number": surah_data["number"],
            "name_ar": surah_data["name_ar"],
            "name_en": surah_data["name_en"],
            "ayahs_count": len(surah_data["ayahs"]),
            "page_start": surah_data["page_start"],
            "page_end": surah_data["page_end"],
            "file": f"surahs/{s_no:03d}.json"
        })

    manifest = {
        "riwayah": riwayah,
        "edition": "King Fahd Glorious Quran Printing Complex (KFGQPC)",
        "total_surahs": len(manifest_surahs),
        "total_ayahs": sum(s["ayahs_count"] for s in manifest_surahs),
        "surahs": manifest_surahs
    }
    manifest_path = target_dir / "manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"[+] {riwayah.upper()} text processing complete: 114 surahs saved, {manifest['total_ayahs']} ayahs.")

def download_page_coordinates(riwayah="hafs", start_page=1, end_page=604, max_workers=10):
    print(f"[*] Downloading {riwayah.upper()} ayah coordinate polygons (pages {start_page}-{end_page})...")
    target_dir = (HAFS_DIR if riwayah == "hafs" else WARSH_DIR) / "coordinates"
    target_dir.mkdir(parents=True, exist_ok=True)

    url_template = URL_COORDS_HAFS if riwayah == "hafs" else URL_COORDS_WARSH

    def download_page(page_num):
        dest = target_dir / f"{page_num:03d}.json"
        if dest.exists() and dest.stat().st_size > 50:
            return page_num, True
        url = url_template.format(page=page_num)
        try:
            content = fetch_url(url)
            # Validate JSON
            data = json.loads(content.decode('utf-8'))
            with open(dest, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return page_num, True
        except Exception as e:
            return page_num, False

    pages = list(range(start_page, end_page + 1))
    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_page, p): p for p in pages}
        for fut in as_completed(futures):
            p_num, ok = fut.result()
            if ok:
                success_count += 1
            if success_count % 50 == 0 or success_count == len(pages):
                print(f"    Progress: {success_count}/{len(pages)} pages processed.")

    print(f"[+] {riwayah.upper()} coordinates downloaded: {success_count}/{len(pages)} pages.")

def download_all_svgs(riwayah="hafs", start_page=1, end_page=604, max_workers=15):
    """Downloads all 604 SVG pages concurrently."""
    print(f"[*] Downloading {riwayah.upper()} SVG pages ({start_page}-{end_page}) with {max_workers} threads...")
    target_dir = (HAFS_DIR if riwayah == "hafs" else WARSH_DIR) / "svg"
    target_dir.mkdir(parents=True, exist_ok=True)

    url_template = URL_SVG_HAFS if riwayah == "hafs" else URL_SVG_WARSH

    def download_svg(page_num):
        dest = target_dir / f"{page_num:03d}.svg"
        if dest.exists() and dest.stat().st_size > 100:
            return page_num, True
        url = url_template.format(page=page_num)
        try:
            content = fetch_url(url)
            with open(dest, 'wb') as f:
                f.write(content)
            return page_num, True
        except Exception as e:
            return page_num, False

    pages = list(range(start_page, end_page + 1))
    success_count = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(download_svg, p): p for p in pages}
        for fut in as_completed(futures):
            p_num, ok = fut.result()
            if ok:
                success_count += 1
            if success_count % 50 == 0 or success_count == len(pages):
                print(f"    Progress: {success_count}/{len(pages)} SVGs saved.")

    print(f"[+] {riwayah.upper()} SVGs downloaded: {success_count}/{len(pages)} pages.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Download & process Quran datasets")
    parser.add_argument("--texts-only", action="store_true", help="Only process text JSONs")
    parser.add_argument("--coords-only", action="store_true", help="Only process coordinate JSONs")
    parser.add_argument("--sample-svgs", action="store_true", help="Download sample SVG pages")
    parser.add_argument("--all-svgs", action="store_true", help="Download all 604 SVG pages")
    args = parser.parse_args()

    if not args.coords_only and not args.sample_svgs and not args.all_svgs:
        process_texts("hafs")
        process_texts("warsh")

    if not args.texts_only and not args.sample_svgs and not args.all_svgs:
        download_page_coordinates("hafs", 1, 604)
        download_page_coordinates("warsh", 1, 604)

    if args.sample_svgs:
        download_all_svgs("hafs", 1, 15)
        download_all_svgs("warsh", 1, 15)

    if args.all_svgs:
        download_all_svgs("hafs", 1, 604)
        download_all_svgs("warsh", 1, 604)
