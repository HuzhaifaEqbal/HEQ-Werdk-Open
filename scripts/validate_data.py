import json
import glob
import os
import sys

# Ensure UTF-8 output on all systems including Windows cp1256
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def main():
    print("[INFO] Starting Data Integrity Validation...")
    errors = 0

    # 1. Check all JSON files parse cleanly
    json_files = [
        f for f in glob.glob('**/*.json', recursive=True)
        if not f.startswith('.git')
        and not f.startswith('HEQWERDK')
        and 'node_modules' not in f
    ]
    print(f"[INFO] Scanning {len(json_files)} JSON files...")

    for jf in json_files:
        try:
            with open(jf, 'r', encoding='utf-8') as f:
                json.load(f)
        except Exception as e:
            print(f"[ERROR] Invalid JSON in {jf}: {e}")
            errors += 1

    # 2. Check manifest paths
    manifests = [
        ('tajweed/manifest.json', 'tajweed'),
        ('fiqh/manifest.json', 'fiqh'),
        ('AlSera_Alnabaoia/manifest.json', 'AlSera_Alnabaoia'),
        ('ALnawoi/manifest.json', 'ALnawoi'),
        ('seerah_map/manifest.json', 'seerah_map'),
        ('quran_oasis/manifest.json', 'quran_oasis'),
        ('quran/hafs/manifest.json', 'quran/hafs'),
        ('quran/warsh/manifest.json', 'quran/warsh')
    ]

    for mf, base_dir in manifests:
        if not os.path.exists(mf):
            print(f"[ERROR] Manifest not found: {mf}")
            errors += 1
            continue
        try:
            with open(mf, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to parse manifest {mf}: {e}")
            errors += 1
            continue

        if 'surahs' in data and base_dir.startswith('quran'):
            for s in data['surahs']:
                sf = s.get('file', '')
                fp = os.path.join(base_dir, sf)
                if not os.path.exists(fp):
                    print(f"[ERROR] Missing surah file in {mf}: {fp}")
                    errors += 1

        if 'modules' in data:
            for mod in data['modules']:
                mid = mod.get('id', '')
                for fl in mod.get('files', []):
                    fp = os.path.join(base_dir, mid, fl.get('file', ''))
                    if not os.path.exists(fp):
                        print(f"[ERROR] Missing file in {mf}: {fp}")
                        errors += 1

        if 'nodes' in data:
            for node in data['nodes']:
                nid = node.get('id', '')
                for fl in node.get('files', []):
                    fp = os.path.join(base_dir, nid, fl.get('file', ''))
                    if not os.path.exists(fp):
                        print(f"[ERROR] Missing file in {mf}: {fp}")
                        errors += 1

        if 'chapters' in data:
            for ch in data['chapters']:
                cf = ch.get('file', '')
                fp = os.path.join(base_dir, cf)
                if not os.path.exists(fp):
                    print(f"[ERROR] Missing chapter in {mf}: {fp}")
                    errors += 1

        if 'files' in data and base_dir in ('ALnawoi', 'seerah_map'):
            for fl in data['files']:
                fp = os.path.join(base_dir, fl.get('file', ''))
                if not os.path.exists(fp):
                    print(f"[ERROR] Missing file in {mf}: {fp}")
                    errors += 1

        if 'available_ajzaa' in data and base_dir == 'quran_oasis':
            for ajz in data['available_ajzaa']:
                pth = ajz.get('path', '')
                ajz_dir = os.path.join(base_dir, pth)
                if not os.path.isdir(ajz_dir):
                    print(f"[ERROR] Missing juz folder in {mf}: {ajz_dir}")
                    errors += 1

    # 3. Verify zero ayahMeanings in quran_oasis
    for qf in glob.glob('quran_oasis/juz_*/*.json'):
        with open(qf, 'r', encoding='utf-8') as f:
            if 'ayahMeanings' in f.read():
                print(f"[ERROR] Found ayahMeanings in: {qf}")
                errors += 1

    if errors == 0:
        print("[SUCCESS] All JSON files valid and manifest references match 100%.")
        sys.exit(0)
    else:
        print(f"[FAILURE] Found {errors} errors during validation.")
        sys.exit(1)

if __name__ == '__main__':
    main()
