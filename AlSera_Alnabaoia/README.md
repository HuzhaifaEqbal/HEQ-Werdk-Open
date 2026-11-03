# 📜 واحة السيرة النبوية الشريفة — دليل المطور واستدعاء البيانات
## (Prophetic Seerah Interactive Curriculum — Developer & API Integration Guide)

> **المستودع:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **الرابط المباشر (Raw):** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/AlSera_Alnabaoia/`  
> **شبكة التوزيع (jsDelivr CDN):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/`  
> **الهيكل:** 8 أبواب زمنية تضم 59 درساً تفاعلياً | **الصيغة:** JSON (UTF-8)

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
مسار السيرة النبوية بيقدملك تسلسل زمني مرتب لحياة النبي ﷺ، مقسم لـ **8 أبواب زمنية** (بمجموع 59 درساً تفاعلياً) بتبدأ من أحوال مكة قبل البعثة والمولد والنشأة، ومروراً بالهجرة وبناء المدينة والغزوات، لعند حجة الوداع والوفاة ﷺ.
كل درس فيه بطاقات شرح (`concept`) موثقة من مصادر السيرة المحققة (ابن هشام والرحيق المختوم)، ومعها أسئلة تفاعلية وسيناريوهات وترتيب للأحداث لتسهيل الفهم والحفظ.

### 🇬🇧 In English
The Prophetic Seerah Curriculum offers a chronological educational pathway through the life of Prophet Muhammad ﷺ, structured across **8 historical chapters** containing 59 interactive lessons from pre-Islamic Mecca to the Farewell Pilgrimage and the passing of the Prophet ﷺ. Concept cards include historical citations, followed by interactive exercises.

---

## ⚡ روابط الاستدعاء المباشر (Direct Endpoints)

### 1. عبر خادم GitHub الخام (Raw GitHub API)
```http
https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/AlSera_Alnabaoia/{CHAPTER_FILE}
```
**أمثلة:**
* الباب 1 (المولد والنشأة):
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/AlSera_Alnabaoia/01_makka_w_wlada_alrasul.json
  ```
* الباب 4 (الهجرة وبناء المدينة):
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/AlSera_Alnabaoia/04_alhijra_wbina_almadina.json
  ```

### 2. عبر شبكة التوزيع السحابية (jsDelivr CDN)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/{CHAPTER_FILE}
```
**مثال:**
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/01_makka_w_wlada_alrasul.json
```

### 3. الفهرس المجمع (Dynamic Discovery Manifest)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/manifest.json
```

---

## 📐 هيكل بيانات السيرة (JSON Schema)

كل ملف باب يحتوي على مصفوفة دروس تفاعلية:

```json
[
  {
    "lesson_id": "01_makka_before_islam",
    "title": "مكة والبيت الحرام في زمن قريش",
    "steps": [
      {
        "type": "concept",
        "title": "مكانة مكة وقريش في جزيرة العرب",
        "content": "كانت مكة مركزاً تجارياً ودينياً بفضل الكعبة المشرفة ورحلتي الشتاء والصيف...",
        "sources": [
          {
            "book": "الرحيق المختوم - المباركفوري",
            "link": "https://shamela.ws/book/115/15"
          }
        ]
      },
      {
        "type": "question",
        "question_type": "scrambled_words",
        "question_text": "رتب أحداث تجديد بناء الكعبة الشريفة بالترتيب الصحيح:",
        "correct_order": [
          "سيل جارف يصدع جدران الكعبة",
          "اتفاق قريش على إعادة البناء بمال حلال",
          "الخلاف على من يضع الحجر الأسود",
          "تحكيم أول داخل وهو النبي الأمين ﷺ"
        ],
        "explanation": "أعادت قريش بناء الكعبة واختلفت في وضع الحجر الأسود حتى رأت محمداً ﷺ فرضيت بحكمه."
      }
    ]
  }
]
```

---

## 💻 أكواد الاستدعاء الجاهزة (Ready Code Snippets)

### 📱 Flutter / Dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class SeerahService {
  static const String baseUrl = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia';

  // 1. Fetch Dynamic Manifest
  static Future<Map<String, dynamic>> fetchManifest() async {
    final response = await http.get(Uri.parse('$baseUrl/manifest.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Seerah manifest');
  }

  // 2. Fetch Specific Seerah Chapter
  static Future<List<dynamic>> fetchChapter(String chapterFile) async {
    final response = await http.get(Uri.parse('$baseUrl/$chapterFile'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Seerah chapter: $chapterFile');
  }
}
```

### 🌐 JavaScript / TypeScript
```typescript
const SEERAH_BASE_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia';

async function getSeerahChapter(chapterFile: string) {
  const response = await fetch(`${SEERAH_BASE_URL}/${chapterFile}`);
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  return await response.json();
}

// Example usage:
getSeerahChapter('01_makka_w_wlada_alrasul.json')
  .then(lessons => console.log('Loaded lessons count:', lessons.length));
```

### 🐍 Python
```python
import requests

SEERAH_BASE_URL = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia"

def fetch_seerah_chapter(chapter_file: str) -> list:
    url = f"{SEERAH_BASE_URL}/{chapter_file}"
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return resp.json()

# Example:
chapter = fetch_seerah_chapter("04_alhijra_wbina_almadina.json")
print("Total lessons in migration chapter:", len(chapter))
```

---

## 🗂️ فهرس الأبواب الزمنية (Chronological Chapters Index)

| الباب (#) | اسم الملف (File) | العنوان بالعربية | English Title | عدد الدروس الفعلي |
|---|---|---|---|---|
| 01 | `01_makka_w_wlada_alrasul.json` | مكة قبل البعثة والمولد والنشأة | Pre-Islamic Mecca, Birth & Upbringing | 8 دروس |
| 02 | `02_alwahy_waldawa_fi_makka.json` | بدء الوحي والدعوة في مكة | Revelation & Meccan Call | 10 دروس |
| 03 | `03_altamhid_lilhijra.json` | التمهيد للهجرة والبيعات | Preparations for Hijrah | 5 دروس |
| 04 | `04_alhijra_wbina_almadina.json` | الهجرة وبناء المجتمع المدني | Migration & Establishing Medina | 8 دروس |
| 05 | `05_tathbit_almujtama_waldifaa.json` | تثبيت المجتمع والدفاع عن الرسالة | Defending the Message & Battles | 9 دروس |
| 06 | `06_ittisaa_aldawa_wfath_makka.json` | اتساع الدعوة وفتح مكة | Spread of Islam & Mecca Conquest | 8 دروس |
| 07 | `07_hajjat_alwadaa_walwufud.json` | عام الوفود وحجة الوداع | Delegations & Farewell Pilgrimage | 6 دروس |
| 08 | `08_akhir_hayat_alrasul_wathar_alrisala.json` | آخر حياة النبي ﷺ وأثر الرسالة | Final Days & Enduring Legacy | 5 دروس |
| **المجموع** | **8 ملفات** | **مسار السيرة النبوية كاملاً** | **Complete Seerah Pathway** | **59 درساً** |

---

هذا المحتوى مرخّص وفق رخصة CC BY-NC 4.0، باستثناء ما هو مذكور في ملف LICENSE (الخط، مواد الأطراف الأخرى، الهوية البصرية، الصور المجمّعة). التفاصيل في LICENSE وATTRIBUTION.md.
