# 📚 دليل وهيكل بيانات مسار السيرة النبوية (Seerah Learning Path Data)
## (Seerah Chronological Learning Path Schema & Integration Guide)

> ### 📌 الوظائف والمهام الأساسية لهذا الملف (File Functions & Scope):
> * **دليل تكامل بيانات السيرة النبوية:** توثيق شجرة الملفات والدروس الثمانية في صيغة UTF-8 JSON.
> * **مخطط البيانات (JSON Schema):** تفاصيل معرّف الدرس (`lesson_id`)، العناوين، ومصفوفة الخطوات المتناوبة (`steps`).
> * **توثيق أنواع الأسئلة:** خيارات متعددة، سيناريوهات تاريخية، ملء الفراغات، وترتيب الأحداث.
> * **الفئة المستهدفة:** مهندسو الواجهة الخلفية، مطورو التطبيقات، ومهندسو البيانات.

---

## Folder tree

```text
Alsira_Alnabauia/
├── promt_for_data.md                     # Original project brief
├── seerah_path_plan.md                   # Course plan and editorial rules
├── README_data.md                        # This data and integration guide
└── data/
    ├── 01_makka_w_wlada_alrasul.json      # Mecca, birth, family and upbringing
    ├── 02_alwahy_waldawa_fi_makka.json    # Revelation and Meccan mission
    ├── 03_altamhid_lilhijra.json          # Yathrib contacts and pledges
    ├── 04_alhijra_wbina_almadina.json    # Migration and Medina community
    ├── 05_tathbit_almujtama_waldifaa.json # Battles, treaties and defense
    ├── 06_ittisaa_aldawa_wfath_makka.json # Outreach, campaigns and Mecca
    ├── 07_hajjat_alwadaa_walwufud.json   # Tabuk, delegations and final Hajj
    └── 08_akhir_hayat_alrasul_wathar_alrisala.json # Final illness and legacy
```

File names use lowercase Latin transliteration, digits, and underscores to avoid Unicode filename issues on servers. Keep Arabic in the user-facing titles and lesson text.

## Data shape

Each file is a JSON array of lessons. Each lesson has a stable `lesson_id`, an Arabic `title`, and an ordered `steps` array. Current lessons have six steps, alternating `concept`, `question`, and ending with a question.

```json
{
  "lesson_id": "01_example_lesson",
  "title": "عنوان الدرس",
  "steps": [
    {
      "type": "concept",
      "title": "عنوان البطاقة",
      "content": "نص الشرح",
      "sources": [{ "book": "اسم المصدر", "link": "https://example.org/source" }]
    },
    {
      "type": "question",
      "question_type": "multiple_choice",
      "question_text": "نص السؤال",
      "options": ["خيار 1", "خيار 2", "خيار 3"],
      "correct_answer_index": 0,
      "explanation": "سبب الإجابة"
    }
  ]
}
```

## Question fields

- `multiple_choice`: `options` and zero-based `correct_answer_index`.
- `scenario_based`: `scenario_text`, `options`, and zero-based `correct_answer_index`.
- `fill_in_the_blanks`: `answer`.
- `scrambled_words`: `correct_order` in chronological order.
- Every question has `question_type`, `question_text`, and `explanation`.

## Sources, images, and narration review

- Every concept card includes a `sources` array with a source name and link. Prefer a direct hadith, Quran passage, or a relevant Seerah source page when adding material.
- Add `image_url` only where a map or illustration helps the learner, using an agreed CDN placeholder such as `{{CDN_IMAGE_BADR_MAP}}`. Replace placeholders when the approved assets are available.
- Do not present an unverified report as established fact. If a weak report is included for editorial review, put the exact label **`رواية ضعيفة`** immediately beside its text and cite the source of the weakness judgment when available. The current files avoid relying on identified weak reports; disputed details are described cautiously or omitted.
- Avoid asserting disputed exact dates. State the well-known period and explain uncertainty where needed.

## Adding or changing content

1. Add the lesson to the chronological door file, keeping `lesson_id` unique across the project.
2. Keep 5–8 steps per lesson; use an even count if alternating concept and question cards from a concept card.
3. Provide sources on every concept card and vary question types across a lesson.
4. Use lowercase Latin transliteration for new file names and stable IDs; use Arabic for learner-facing content.
5. Update this README and `seerah_path_plan.md` if the folder structure or door sequence changes.

The JSON files were parsed successfully after generation. Integrators can load each file as a lesson array and render `steps` in their stored order.
