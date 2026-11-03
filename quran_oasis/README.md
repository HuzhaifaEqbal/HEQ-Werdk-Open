# 🕋 واحة القرآن الكريم — دليل المطور واستدعاء بيانات الحفظ المصغر
## (Quran Oasis Micro-Hifz Curriculum — Developer & API Integration Guide)

> **المستودع:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **الرابط المباشر (Raw):** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/quran_oasis/`  
> **شبكة التوزيع (jsDelivr CDN):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/`  
> **الخط والرسم:** الرسم العثماني المصحفي  
> **الضابط الأساسي:** **ممنوع البعثرة مطلقاً (STRICTLY NO SCRAMBLING)**  
> **الصيغة:** JSON (UTF-8)

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
### طريقة استخدام العقد القرآنية

العقد الموجودة في هذا المستودع مبنية وفق خوارزميات المشروع، لذلك عدد العقد وطول كل عقدة مو ثابتين في جميع السور والدروس.

فينا نستخدم العقد الجاهزة كما هي، أو نعدّل طريقة تقسيمها حسب احتياجات التطبيق والخوارزمية المستخدمة. ويمكن استدعاء كل عقدة بشكل مستقل في Flutter أو أي إطار عمل آخر، بدل تحميل جميع العقد دفعة واحدة.

أما تفسير الآيات، فيمكن جلبه عند الحاجة من خلال API يختاره المطوّر، بدلاً من تخزين تفسير مكرر داخل ملفات العقد. في الأمثلة التوضيحية سنستخدم الاسم `your_API_ForTafseer` للدلالة على واجهة التفسير التي يحددها المطوّر؛ وهذا اسم بديل وليس API جاهزاً مقدّماً من المستودع.

> **قاعدة شرعية صارمة:** يُحظر تماماً أي نشاط لبعثرة أو إعادة ترتيب كلمات القرآن الكريم أو الآيات احتراماً لقدسية كلام الله عز وجل. الأنشطة المعتمدة تقتصر على ملء الفراغات الموضعية ومعرفة الآية التالية.

### 🇬🇧 In English
### How to Use Quranic Nodes

The nodes in this repository are structured according to the project's chunking algorithms. Therefore, the number of nodes and the length of each node are not fixed across all Surahs and lessons.

Developers can use the provided nodes as they are, or adapt the segmentation to match their application requirements and algorithms. Each node can be fetched independently in Flutter or other frameworks without downloading the full dataset at once.

For verse interpretations (Tafseer), applications can fetch them on-demand via a developer-selected API rather than duplicating text within node files. In illustrative examples, `your_API_ForTafseer` serves as a placeholder for the developer's chosen Tafseer endpoint, not a bundled service.

> **Sacred Rule:** Strictly no scrambled words or disordered verses are permitted in any activity, preserving the sanctity and exact order of the Noble Quran.

---

## ⚡ روابط الاستدعاء المباشر (Direct Endpoints)

### 1. عبر خادم GitHub الخام (Raw GitHub API)
```http
https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/quran_oasis/{JUZ_FOLDER}/{NODE_FILE}
```
**أمثلة:**
* عقدة النبأ الأولى (جزء 30):
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/quran_oasis/juz_30/node_078_01.json
  ```
* عقدة الإخلاص (جزء 30):
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/quran_oasis/juz_30/node_112_01.json
  ```

### 2. عبر شبكة التوزيع (jsDelivr CDN)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/{JUZ_FOLDER}/{NODE_FILE}
```
**مثال:**
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_30/node_112_01.json
```

### 3. الفهرس المجمع (Dynamic Discovery Manifest)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/manifest.json
```

---

## 📐 هيكل بيانات العقدة القرآنية (JSON Node Schema)

```json
{
  "nodeId": "node_112_01",
  "title": "سورة الإخلاص: صفة الرحمن وتوحيد الذات والصفات",
  "surahId": 112,
  "ayahStart": 1,
  "ayahEnd": 4,
  "activities": [
    {
      "activityId": "act_112_01_01",
      "type": "fill_in_the_blank",
      "ayahNumber": 1,
      "missingWordPosition": 4,
      "options": [
        "أَحَدٌ",
        "وَاحِدٌ",
        "عَلِيمٌ",
        "قَدِيرٌ"
      ]
    },
    {
      "activityId": "act_112_01_02",
      "type": "next_ayah",
      "currentAyahNumber": 1,
      "correctNextAyahNumber": 2,
      "wrongOptionsAyahNumbers": [
        3,
        4
      ]
    }
  ],
  "tutorContext": {
    "surahName": "الإخلاص",
    "juz": 30,
    "theme": "بيان صفة الله تعالى وتوحيده الخالص: الأحد الصمد المنزه عن الولد والوالد والمكافئ والمثيل"
  }
```

> 📌 **ملاحظات حول بنية العقدة و `tutorContext`:**
> - الحقل الأساسي في `tutorContext` هو `theme` الذي يقدم فكرة موضوعية موجزة عن مقطع الآيات، وبعض الملفات تحتوي أيضاً على حقول وصفية إضافية مثل `surahName` و `juz`.
> - ملفات التحديات الصوتية (مثل `node_078_09_voice.json`) تتبع بنية مخصصة بنوع `voice_challenge`، ويكون نص الإرشاد فيها مدمجاً داخل النشاط نفسه.
> - تفاسير الآيات لا تُخزّن داخل ملفات العقد لتجنب التكرار ولإتاحة الحرية للمطوّر في اختيار مصدر التفسير المناسب عبر API خارجي.

---

## 💻 أكواد الاستدعاء الجاهزة (Ready Code Snippets)

### 📱 Flutter / Dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class QuranOasisService {
  static const String baseUrl = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis';

  // 1. Fetch Dynamic Manifest
  static Future<Map<String, dynamic>> fetchManifest() async {
    final response = await http.get(Uri.parse('$baseUrl/manifest.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Quran Oasis manifest');
  }

  // 2. Fetch Specific Quran Node
  static Future<Map<String, dynamic>> fetchNode(String juzFolder, String nodeFile) async {
    final response = await http.get(Uri.parse('$baseUrl/$juzFolder/$nodeFile'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Quran node: $nodeFile');
  }

  // 3. Fetch Tafseer upon user demand from developer-chosen API
  static Future<String> fetchTafseer(int surah, int ayah) async {
    // your_API_ForTafseer is a placeholder for your chosen Tafseer service
    final response = await http.get(Uri.parse('https://your_API_ForTafseer?surah=$surah&ayah=$ayah'));
    if (response.statusCode == 200) {
      final data = jsonDecode(utf8.decode(response.bodyBytes));
      return data['text'] ?? '';
    }
    return '';
  }
}
```

### 🌐 JavaScript / TypeScript
```typescript
const QURAN_BASE_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis';

async function getQuranNode(juzFolder: string, nodeFile: string) {
  const response = await fetch(`${QURAN_BASE_URL}/${juzFolder}/${nodeFile}`);
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  return await response.json();
}

// Example usage:
getQuranNode('juz_30', 'node_112_01.json')
  .then(data => console.log('Loaded node activities:', data.activities.length));
```

### 🐍 Python
```python
import requests

QURAN_BASE_URL = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis"

def fetch_quran_node(juz_folder: str, node_file: str) -> dict:
    url = f"{QURAN_BASE_URL}/{juz_folder}/{node_file}"
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding = 'utf-8'
    return resp.json()

# Example:
node = fetch_quran_node("juz_30", "node_112_01.json")
print("Surah ID:", node['surahId'], "Title:", node['title'])
```

---

## 🗂️ فهرس الأجزاء والسور (Ajzaa & Surahs Index)

| الجزء (Juz) | المسار (Path) | نطاق السور | عدد الملفات المعتمدة | نوع الأنشطة |
|-------------|--------------|------------|----------------------|--------------|
| **جزء عمّ (Juz 30)** | `juz_30/` | سورة 78 (النبأ) إلى سورة 114 (الناس) | 108 ملفات (107 عقد حفظ + 1 تحدي صوتي) | فراغات + تخمين الآية التالية + تحدي صوتي |
| **جزء تبارك (Juz 29)** | `juz_29/` | سورة 67 (الملك) إلى سورة 77 (المرسلات) | 84 عقدة | فراغات + تخمين الآية التالية |
| **جزء ألم (Juz 1)** | `juz_01/` | سورة 1 (الفاتحة) وبداية سورة 2 (البقرة) | 30 عقدة | فراغات + تخمين الآية التالية |

> 📌 **تنبيه:** باقي مجلدات الأجزاء الموجودة داخل المستودع تُعد مسودات عمل غير مدرجة في الفهرس الرسمي حتى تكتمل مراجعتها وتدقيقها.

---

> ⚠️ **إشعار الترخيص وحقوق الاستخدام:** الترخيص قيد التحديد والمراجعة القانونية من قبل صاحب المشروع لضمان التوافق مع حقوق النشر والمصادر المعتمدة.
