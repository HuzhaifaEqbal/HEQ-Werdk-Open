# 📖 واحة التجويد التفاعلية — دليل المطور واستدعاء البيانات
## (Interactive Tajweed Curriculum — Developer & API Integration Guide)

> **Repository:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **Direct Raw Endpoint:** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/tajweed/`  
> **Global Fast CDN (jsDelivr):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/`  
> **Format:** JSON (UTF-8) | **Total Modules:** 10 | **Total Files:** 50

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
مسار التجويد بيوفرلك منهج عملي متكامل مكوّن من **10 أبواب تعليمية** و **50 ملف JSON**. صممنا الدروس بنظام التعليم المصغر (Micro-learning) مشان يكون التعلم خفيف وسلس؛ كل درس بيبدأ ببطاقة مفهوم (`concept`) مع أمثلة توضيحية، ووراها فوراً سؤال تفاعلي (`question`) لتثبيت الحكم، وكل باب بينتهي باختبار تقييمي كامل (`boss_level`).

### 🇬🇧 In English
The Open Interactive Tajweed Curriculum provides an educational dataset consisting of **10 structured modules** and **50 JSON files**. Designed using a micro-learning pattern, each lesson alternates between bite-sized instructional concepts with audio references and immediate interactive quiz checkpoints. Every module concludes with a comprehensive "Boss Level" evaluation.

---

## ⚡ طرق الاستدعاء المباشر عبر الإنترنت (Direct Fetch Endpoints)

You can consume these JSON datasets directly without downloading the repository using two reliable endpoints:

### 1. عبر خادم GitHub الخام (Raw GitHub API)
```http
https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/tajweed/{MODULE_NAME}/{FILE_NAME}
```
**Example:**
```http
https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/tajweed/01_Basics_and_Makharij/01_intro_and_importance.json
```

### 2. عبر شبكة التوزيع السريعة (jsDelivr CDN)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/{MODULE_NAME}/{FILE_NAME}
```
**Example:**
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/01_Basics_and_Makharij/01_intro_and_importance.json
```

### 3. الفهرس الديناميكي المجمع (Dynamic Discovery Manifest)
To list all modules and files dynamically without hardcoding URLs in your app:
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/manifest.json
```

---

## 📐 هيكل البيانات (JSON Data Schemas)

### 1. ملفات الدروس اليومية (Lesson Files: `01` to `04`)
Each lesson file is a JSON Object with a `steps` array of 10 alternating items (5 concepts + 5 questions):

```json
{
  "steps": [
    {
      "type": "concept",
      "title": "تعريف علم التجويد",
      "content": "التجويد اصطلاحاً هو إخراج كل حرف من مخرجه الدقيق، وإعطاؤه حقه ومستحقه...",
      "example": "قراءة (عَسَى) بدلاً من (عَصَى) هو تغيير للمعنى.",
      "audio_example": "https://heq-cdn.b-cdn.net/quran/al_husary/murattal/001/001.mp3"
    },
    {
      "type": "question",
      "question_type": "multiple_choice",
      "question_text": "ما هو التعريف الاصطلاحي لعلم التجويد عند علماء القراءات؟",
      "options": [
        "إخراج كل حرف من مخرجه مع إعطائه حقه ومستحقه من الصفات.",
        "تحسين الصوت بتلاوة القرآن الكريم ومحاكاة القراء المشهورين.",
        "معرفة معاني الكلمات الغريبة في القرآن لتسهيل الحفظ.",
        "قراءة القرآن بسرعة مع الحفاظ على الحركات الإعرابية."
      ],
      "correct_answer_index": 0,
      "explanation": "التجويد اصطلاحاً هو إخراج كل حرف من مخرجه الدقيق وإعطاؤه حقه ومستحقه."
    }
  ]
}
```

### 2. ملفات اختبار الزعيم الملكي (Boss Level Files: `05_boss_level_*.json`)
Boss Level files are directly formatted as a JSON Array of 10 evaluation questions:

```json
[
  {
    "id": "q_makharij_01",
    "type": "multiple_choice",
    "question_text": "كم عدد مخارج الحروف العامة المتفق عليها عند جمهور علماء التجويد؟",
    "options": ["خمسة مخارج", "ثلاثة مخارج", "سبعة عشر مخرجاً", "أربعة مخارج"],
    "correct_answer_index": 0,
    "explanation": "المخارج العامة خمسة: الجوف، الحلق، اللسان، الشفتان، الخيشوم."
  }
]
```

---

## 💻 أكواد الاستدعاء الجاهزة (Ready Code Snippets)

### 📱 Flutter / Dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class TajweedService {
  static const String baseUrl = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed';

  // 1. Fetch Dynamic Manifest
  static Future<Map<String, dynamic>> fetchManifest() async {
    final response = await http.get(Uri.parse('$baseUrl/manifest.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Tajweed manifest');
  }

  // 2. Fetch Specific Lesson
  static Future<Map<String, dynamic>> fetchLesson(String module, String file) async {
    final response = await http.get(Uri.parse('$baseUrl/$module/$file'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load lesson: $file');
  }
}
```

### 🌐 JavaScript / TypeScript / Node.js
```typescript
const BASE_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed';

// Fetch specific lesson data
async function getTajweedLesson(moduleName: string, fileName: string) {
  try {
    const response = await fetch(`${BASE_URL}/${moduleName}/${fileName}`);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching Tajweed lesson:', error);
  }
}

// Example usage:
getTajweedLesson('01_Basics_and_Makharij', '01_intro_and_importance.json')
  .then(lesson => console.log('Loaded steps:', lesson.steps.length));
```

### 🐍 Python
```python
import requests

BASE_URL = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed"

def load_tajweed_lesson(module_id: str, file_name: str) -> dict:
    url = f"{BASE_URL}/{module_id}/{file_name}"
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return resp.json()

# Example:
lesson = load_tajweed_lesson("03_Nun_Sakinah_and_Tanween", "01_izhar_halqi.json")
print(f"Loaded lesson with {len(lesson['steps'])} steps")
```

---

## 🗂️ فهرس الأبواب والملفات (Directory Structure Index)

| # | الباب (Module ID) | العنوان بالعربية | English Title | ملفات الدروس (Lessons) |
|---|-------------------|-------------------|---------------|-------------------------|
| 1 | `01_Basics_and_Makharij` | أساسيات ومخارج الحروف | Basics & Articulations | 4 دروس + Boss Level |
| 2 | `02_Sifat_Al_Huroof` | صفات الحروف | Letter Characteristics | 4 دروس + Boss Level |
| 3 | `03_Nun_Sakinah_and_Tanween` | النون الساكنة والتنوين | Nun Sakinah & Tanween | 4 دروس + Boss Level |
| 4 | `04_Meem_Sakinah_and_Mushaddadah` | الميم الساكنة والمشددة | Meem Sakinah Rules | 4 دروس + Boss Level |
| 5 | `05_Madd_Rules_Part_1` | أحكام المد (الجزء 1) | Madd Rules (Part 1) | 4 دروس + Boss Level |
| 6 | `06_Madd_Rules_Part_2` | أحكام المد (الجزء 2) | Madd Rules (Part 2) | 4 دروس + Boss Level |
| 7 | `07_Tafkheem_and_Tarqeeq` | التفخيم والترقيق | Tafkheem & Tarqeeq | 4 دروس + Boss Level |
| 8 | `08_Relations_Between_Letters` | العلاقات بين الحروف | Letter Relationships | 4 دروس + Boss Level |
| 9 | `09_Hamzat_and_Waqf` | الهمزات والوقف | Hamzah & Waqf | 4 دروس + Boss Level |
| 10 | `10_Maqtoo_Mawsool_and_Conclusion` | المقطوع والموصول والخاتمة | Maqtoo, Mawsool & Conclusion | 4 دروس + Boss Level |

## 📚 المراجع العلمية المعتمدة لمنهج التجويد (Scholarly References)

المحتوى العلمي للتجويد مستنبط وفق رواية حفص عن عاصم من طريق الشاطبية، استناداً إلى أمهات المتون والكتب التراثية المعتمدة:
1. **المقدمة الجزرية (متن الجزرية)** — الإمام شمس الدين محمد بن محمد بن الجزري (ت 833 هـ).
2. **تحفة الأطفال والغلمان في تجويد القرآن** — الشيخ سليمان بن حسين الجمزوري (ت بعد 1198 هـ).
3. **التحديد في الإتقان والتسديد** — الإمام أبو عمرو عثمان بن سعيد الداني (ت 444 هـ).
4. **غاية المريد في علم التجويد** — الشيخ عطية قابل نصر.
5. **حق التلاوة** — الشيخ حسني شيخ عثمان.
6. **أحكام قراءة القرآن الكريم** — الشيخ محمود خليل الحصري.

---

هذا المحتوى مرخّص وفق رخصة CC BY-NC 4.0، باستثناء ما هو مذكور في ملف LICENSE (الخط، مواد الأطراف الأخرى، الهوية البصرية، الصور المجمّعة). التفاصيل في LICENSE وATTRIBUTION.md.
