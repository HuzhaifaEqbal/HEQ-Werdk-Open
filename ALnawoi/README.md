# 📜 الأربعون النووية — دليل المطور واستدعاء البيانات
## (An-Nawawi 40 Hadiths Dataset — Developer & API Integration Guide)

> **المستودع:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **الرابط المباشر (Raw):** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/ALnawoi/`  
> **شبكة التوزيع (jsDelivr CDN):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/`  
> **الصيغة:** JSON (UTF-8) | **عدد الأحاديث المعتمدة:** 40 حديثاً | **الميزات:** أسانيد، تخريج، وقضايا فقهية

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
بهاد المسار جمعنالك أحاديث **الأربعين النووية** للإمام النووي رحمه الله بملفات JSON مرتبة ومهيكلة.
كل حديث فيه المتن مشكول بالكامل، والتخريج، وسلسلة السند (`isnadChain`) من شيخ المصنف لعند الصحابي، ومفردات الكلمات الصعبة، والفوائد الفقهية والتربوية المستنبطة من كل حديث.

> 📌 **تنبيه بخصوص عدد الأحاديث:**  
> هاد الإصدار فيه حالياً **40 حديثاً** موزعين على 4 دفعات (كل دفعة 10 أحاديث) أو بملف واحد مجمع. المتن المشهور فيه 42 حديث، ونحنا هسع عم ندقق الحديثين 41 و42 لنلحقهم بالمستودع بس نخلص مراجعتهم الحديثية.

### 🇬🇧 In English
This dataset provides a structured digital edition of **Imam Al-Nawawi's Forty Hadiths**. Key features include vocalized Arabic Matn, academic authentication (Takhrij), relational transmission chains (`isnadChain`) with standardized narrator IDs (`narratorId`), extracted jurisprudential subjects (`coreFiqhTopics`), and pedagogical lessons.

> 📌 **Scholarly Note on Hadith Count:**  
> The current release covers **40 hadiths** structured in 4 batches (10 hadiths each). The traditional compilation extends to 42 hadiths; hadiths 41 and 42 are currently undergoing authentication review before inclusion.

---

## ⚡ روابط الاستدعاء المباشر (Direct Endpoints)

### 1. المتن الكامل الموحد (Complete 40 Hadiths in One File)
* **jsDelivr CDN:**
  ```http
  https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_complete.json
  ```
* **Raw GitHub:**
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/ALnawoi/nawawi_40_complete.json
  ```

### 2. الدفعات المقسمة (Batches: 10 Hadiths Each)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_01.json
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_02.json
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_03.json
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_04.json
```

### 3. الفهرس المجمع (Dynamic Discovery Manifest)
```http
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/manifest.json
```

---

## 📐 هيكل سجل الحديث (JSON Hadith Schema)

الملف الكامل عبارة عن مصفوفة JSON تحتوي على كائنات الأحاديث:

```json
[
  {
    "hadithId": "nawawi_40_01",
    "number": 1,
    "title": "إنما الأعمال بالنيات",
    "matn": "عَنْ أَمِيرِ الْمُؤْمِنِينَ أَبِي حَفْصٍ عُمَرَ بْنِ الْخَطَّابِ رَضِيَ اللَّهُ عَنْهُ قَالَ: سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ يَقُولُ: «إِنَّمَا الأَعْمَالُ بِالنِّيَّاتِ...»",
    "primarySahabi": "عمر بن الخطاب رضي الله عنه",
    "takhrij": "رواه البخاري ومسلم في صحيحهما",
    "authenticity": "صحيح متفق عليه",
    "isnadChain": [
      {
        "order": 1,
        "narratorId": "sahabi_umar_ibn_alkhattab",
        "name": "عمر بن الخطاب رضي الله عنه",
        "role": "الصحابي راوي الحديث"
      }
    ],
    "coreFiqhTopics": [
      "اشتراط النية في العبادات",
      "الإخلاص وتجريد القصد لله تعالى"
    ],
    "briefMeaning": "بيان أن صحة الأعمال وقبولها وثوابها مرتبط بصلاح النية والقصد.",
    "pedagogicalPoints": [
      "النية تميز العبادة عن العادة",
      "الهجرة لله ورسوله أصل عظيم"
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

class NawawiHadithService {
  static const String baseUrl = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi';

  static Future<List<dynamic>> fetchAllHadiths() async {
    final response = await http.get(Uri.parse('$baseUrl/nawawi_40_complete.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Nawawi 40 dataset');
  }
}
```

### 🌐 JavaScript / TypeScript
```typescript
const NAWAWI_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_complete.json';

async function getFortyHadiths() {
  const response = await fetch(NAWAWI_URL);
  if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
  return await response.json();
}

// Example usage:
getFortyHadiths().then(hadiths => {
  console.log('Total hadiths loaded:', hadiths.length);
  console.log('Hadith 1 Title:', hadiths[0].title);
});
```

### 🐍 Python
```python
import requests

url = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_complete.json"
resp = requests.get(url)
resp.raise_for_status()
resp.encoding = 'utf-8'
hadiths = resp.json()

print(f"Successfully loaded {len(hadiths)} hadiths.")
```

---

هذا المحتوى مرخّص وفق رخصة CC BY-NC 4.0، باستثناء ما هو مذكور في ملف LICENSE (الخط، مواد الأطراف الأخرى، الهوية البصرية، الصور المجمّعة). التفاصيل في LICENSE وATTRIBUTION.md.
