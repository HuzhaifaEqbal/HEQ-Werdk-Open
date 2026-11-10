---
name: heq-app-builder
description: Build an Islamic app or website (Quran, memorization, Tajweed, Fiqh, Hadith, Seerah, adhkar, recitations) using the open HEQ-Werdk-Open datasets and the HEQ audio CDN. Use when the user asks to build an Islamic / Quran / religious app or site, or simply says "build me an app" while this skill is installed.
---

# HEQ App Builder

You are building an Islamic app **on top of the HEQ-Werdk-Open open dataset repository**
(`https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open`).
The data is ready and reviewed. Your job is the **UI and app logic**. **Never author religious content yourself.**

An Arabic copy of these instructions is in `SKILL.ar.md` next to this file; both say the same thing.

## 1. Ask before you build

If the user has not specified, ask these in **one** message:

1. **Platform:** Flutter (mobile) or web (HTML/JS or React)?
2. **Sections** — which of these do they want?
   - Quran (Hafs or Warsh), including the 604-page mushaf layout
   - Quran Oasis: bite-sized memorization, all 30 juz'
   - Tajweed: 10 modules, 50 lessons
   - Simplified Shafi'i Fiqh: Taharah, Salah, Sawm
   - Imam Nawawi's Forty Hadith
   - Prophetic Seerah: 8 chronological chapters, 59 lessons, plus a geographic map
   - Recitation player (reciters, verse-by-verse or full surahs)
3. **Language / direction:** Arabic RTL only, or Arabic + English?

If the user says "I don't know" or "you decide", default to: **Arabic RTL Flutter app with Quran, Quran Oasis, Tajweed and a recitation player.**

## 2. Where the data comes from

- **Datasets (jsDelivr):**
  `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/{path}`
  For production, pin to a release tag instead of `@main` (latest: `@v1.1.0`) so data shape changes never break the app.
- **Always start from each section's `manifest.json`.** It is the index: file names, order and metadata come from it. **Never guess file names.**
  Manifests: `quran/hafs`, `quran/warsh`, `quran_oasis`, `tajweed`, `fiqh`, `ALnawoi`, `AlSera_Alnabaoia`, `seerah_map`.
- Read each section's `README.md` (and `STRUCTURE_MAP.md` where present) before writing code that parses it, so you match the exact JSON shape.
- Cache fetched JSON locally so the app works offline after the first load.

## 3. Audio

- **Verse-by-verse recitation (HEQ CDN):** `audio/ayah_reciters.json` lists every reciter, style, riwaya and base URL.
  `https://heq-cdn.b-cdn.net/quran/{reciter}/{type}/{surah:03d}/{ayah:03d}.mp3`
  Example: `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/255.mp3`
  The same file also lists verse-by-verse **translation audio** (English, Urdu, Persian, Bosnian, Azerbaijani).
- **Full-surah recitation:** `audio/reciters.json` → `server` + `{surah:03d}.mp3` (HEQ CDN). If a request fails, retry with `fallback_server` + `{surah:03d}.mp3`.
- **Adhkar / duas:** the `audio_url` values already inside the lesson JSON (official Hisn al-Muslim recordings).
- Do not introduce any other audio host (the only exceptions are the `fallback_server` values above and Hisn al-Muslim).

## 4. Religious rules — never break these

1. **The Quran text is never altered** — not one letter or diacritic. Do not "fix", shorten, or type it from memory. Use the repository files as-is.
2. **Hafs ayahs are rendered in the Uthmani font** `fonts/UthmanicHafs_V20.ttf`.
3. **Never invent** hadith, fatwas, tafsir or adhkar. Religious content comes only from the repository. If something is not there, say it is not available.
4. **No depictions** of Allah, prophets, companions or angels — no images, illustrations or avatars.
5. **Show the source** under every hadith or fiqh ruling, exactly as given in the JSON.
6. Fiqh content currently follows the **Shafi'i madhhab** — state this clearly in the app.

## 5. License rules

- Data is licensed **CC BY-NC 4.0**: **non-commercial use only**. No ads or paid subscriptions unless the app owner has separate permission.
- The Uthmani font belongs to the King Fahd Glorious Quran Printing Complex and may be redistributed **unmodified** only — see `fonts/LICENSE_KFGQPC.md`.
- **Do not** use the HEQ Werdk name or logo as the new app's name or branding; branding is excluded from the license.

## 6. Build steps

1. Ask the questions in section 1.
2. Read the `manifest.json` and `README.md` of each chosen section, and `audio/ayah_reciters.json` if audio is needed.
3. Show the user a **short plan**: screens, navigation, and which files feed each screen. Wait for approval.
4. Build: a data layer that fetches from the CDN with local caching, then the screens.
5. Run the app and confirm every section loads its **real** data, not placeholders.
6. Finish with a summary: what was built, how to run it, and what is not done yet.

## 7. Never

- Never bundle large JSON files into source code — fetch them from the CDN.
- Never create mock or placeholder religious content, not even temporarily.
- Never use audio hosts other than those in section 3.
