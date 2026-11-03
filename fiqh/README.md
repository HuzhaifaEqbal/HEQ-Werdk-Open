# ⚖️ واحة الفقه والعبادات اليومية — دليل المطور واستدعاء البيانات
## (Interactive Fiqh & Worship Curriculum — Developer & API Integration Guide)

> **Repository:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **Direct Raw Endpoint:** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/fiqh/`  
> **Global Fast CDN (jsDelivr):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/`  
> **Jurisprudence School (Madhhab):** Shafi'i (المعتمد في الفقه الشافعي مع توثيق المصادر)  
> **Format:** 100% UTF-8 JSON | **Total Nodes:** 5 | **Total Files:** 31

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
مسار الفقه هون بيقدملك منهج فقهي ميسر وموثق لمسائل الطهارة والصلاة والصيام على **المذهب الشافعي**.
الدروس مقسمة بنظام تعليم مصغر (Micro-learning)؛ كل بطاقة شرح (`concept`) فيها نصوص واضحة ومراجع معتمدة من أمهات كتب الشافعية (مثل متن أبي شجاع وفتح القريب)، ومعها أسئلة وسيناريوهات تفاعلية من واقع الحياة (خيارات، سيناريوهات، ترتيب خطوات)، وبنهاية كل عقدة في اختبار تحدي شامل (`boss_level`).
فيك تستدعي ملفات الدروس مباشرة كـ JSON وتدمجها بتطبيقك بضغطة زر.

### 🇬🇧 In English
The Interactive Fiqh & Daily Worship Curriculum is an open-access, verified Islamic jurisprudence educational dataset based on the authoritative **Shafi'i school of jurisprudence**. Built following the gamified micro-learning methodology, every lesson pairs concept cards—referenced with classical jurisprudential sources and electronic library links—with applied interactive questions (multiple choice, real-world case scenarios, fill-in-the-blanks, and step ordering), concluding with comprehensive Boss Level assessments.

---

## ⚡ روابط الاستدعاء المباشر (Direct Endpoints)

### 1. عبر خادم GitHub الخام (Raw GitHub API)
```http
https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/fiqh/{NODE_PATH}/{FILE_NAME}
```
**Examples:**
* Taharah Lesson 1:
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/fiqh/01_Taharah/01_water_and_purity.json
  ```
* Salah Level 1 Lesson 1:
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/fiqh/02_Salah/level_1/01_prayer_times_and_adhan.json
  ```

### 2. عبر شبكة التوزيع السحابية (jsDelivr CDN)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/{NODE_PATH}/{FILE_NAME}
```
**Example:**
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/01_fasting_definition_and_conditions.json
```

### 3. الفهرس الديناميكي المجمع (Dynamic Discovery Manifest)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/manifest.json
```

---

## 📐 هياكل البيانات (JSON Schemas)

### 1. بطاقة الشرح الموثقة بالمصادر (Referenced Concept Step)
```json
{
  "type": "concept",
  "title": "أنواع المياه وحكم كل نوع",
  "content": "تنقسم المياه في الفقه الشافعي إلى أربعة أقسام...",
  "example": "الماء الذي يُجمع من المطر أو مياه العيون والآبار يُعد ماءً مطلقاً...",
  "image_url": "https://your-cdn-assets.com/tahara/water_types.png",
  "sources": [
    {
      "book": "متن أبي شجاع (غاية الاختصار)",
      "link": "https://shamela.ws/book/9780/1"
    },
    {
      "book": "فتح القريب المجيب في شرح ألفاظ التقريب",
      "link": "https://shamela.ws/book/9780"
    }
  ]
}
```

### 2. بطاقة السؤال الاستنتاجي / السيناريو (Scenario-based Question)
```json
{
  "type": "question",
  "question_type": "scenario_based",
  "scenario_text": "توضأ أحمد بماء وُضع فيه زعفران وورد كثير، فتغير لونه ورائحته تغيراً تاماً...",
  "question_text": "ما حكم صحة طهارة أحمد ووضوئه بهذا الماء في المذهب الشافعي؟",
  "options": [
    "لا يصح وضوؤه لأنه ماء طاهر غير مطهر تغير بمخالط طاهر استغنى الماء عنه.",
    "يصح وضوؤه لأن التغير حصل بمادة طاهرة مباركة.",
    "يصح وضوؤه مع الكراهة التنزيهية.",
    "باطل ويعاقب عليه شرعاً."
  ],
  "correct_answer_index": 0,
  "explanation": "الماء المتغير بمخالط طاهر تغيراً يمنع إطلاق اسم الماء عليه طاهر في نفسه غير مطهر لغيره."
}
```

### 3. بطاقة ملء الفراغات بالسحب والإفلات (Fill in the Blanks)
```json
{
  "type": "question",
  "question_type": "fill_in_the_blanks",
  "question_text": "الماء القليل ينجس بمجرد ___ النجاسة، بينما الماء الكثير لا ينجس إلا بـ ___ أحد أوصافه.",
  "correct_words": ["ملاقاة", "تغير"],
  "distractors": ["انفصال", "ركود"],
  "explanation": "القاعدة الفقهية تقتضي التفرقة بين القليل والكثير بملاقاة النجاسة أو تغير الوصف."
}
```

---

## 💻 أكواد الاستدعاء الجاهزة (Ready Code Snippets)

### 📱 Flutter / Dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class FiqhService {
  static const String baseUrl = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh';

  // 1. Fetch Dynamic Manifest
  static Future<Map<String, dynamic>> fetchManifest() async {
    final response = await http.get(Uri.parse('$baseUrl/manifest.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Fiqh manifest');
  }

  // 2. Fetch Specific Fiqh Node Lesson
  static Future<Map<String, dynamic>> fetchLesson(String nodePath, String fileName) async {
    final response = await http.get(Uri.parse('$baseUrl/$nodePath/$fileName'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Fiqh lesson: $fileName');
  }
}
```

### 🌐 JavaScript / TypeScript
```typescript
const FIQH_BASE_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh';

async function getFiqhLesson(nodePath: string, fileName: string) {
  const response = await fetch(`${FIQH_BASE_URL}/${nodePath}/${fileName}`);
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  return await response.json();
}

// Example usage:
getFiqhLesson('01_Taharah', '01_water_and_purity.json')
  .then(data => console.log('Loaded steps:', data.steps.length));
```

### 🐍 Python
```python
import requests

FIQH_BASE_URL = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh"

def fetch_fiqh_file(node_path: str, file_name: str) -> dict:
    url = f"{FIQH_BASE_URL}/{node_path}/{file_name}"
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return resp.json()

# Example:
data = fetch_fiqh_file("04_Sawm/level_1", "01_fasting_definition_and_conditions.json")
print("Lesson title:", data['steps'][0]['title'])
```

---

## 🗂️ فهرس العقد والملفات المتاحة (Nodes & Files Registry)

| العقدة (Node) | المسار (Path) | عدد الملفات | المحتوى العلمي |
|---------------|--------------|-------------|----------------|
| **الطهارة** | `01_Taharah/` | 6 ملفات | المياه، الوضوء، النواقض، الغسل، التيمم، و Boss Level |
| **الصلاة (المستوى 1)** | `02_Salah/level_1/` | 6 ملفات | المواقيت، الشروط، الأركان، السنن، المبطلات، و Boss Level |
| **الصلاة (المستوى 2)** | `02_Salah/level_2/` | 6 ملفات | الجماعة، المسافر، الجمعة، الجنائز والعيدين، السهو، و Boss Level |
| **الصيام (المستوى 1)** | `04_Sawm/level_1/` | 6 ملفات | الشروط، الرؤية، النية والأركان، السنن، المفطرات، و Boss Level |
| **الصيام (المستوى 2)** | `04_Sawm/level_2/` | 7 ملفات | الأعذار، الكفارة، النوافل والمحرم، الاعتكاف، النذر، Boss، وملحق إثرائي |

---

هذا المحتوى مرخّص وفق رخصة CC BY-NC 4.0، باستثناء ما هو مذكور في ملف LICENSE (الخط، مواد الأطراف الأخرى، الهوية البصرية، الصور المجمّعة). التفاصيل في LICENSE وATTRIBUTION.md.
