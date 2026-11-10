# 🌟 الوقف التقني الإسلامي — بيانات للاستخدام غير التجاري
# Islamic Tech Waqf — Datasets for Non-Commercial Use (CC BY-NC 4.0)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Format](https://img.shields.io/badge/format-JSON%20UTF--8-blue.svg)]()
[![CDN](https://img.shields.io/badge/CDN-jsDelivr%20Global-orange.svg)]()
[![Platform](https://img.shields.io/badge/supports-Flutter%20%7C%20Web%20%7C%20AI%20Models-purple.svg)]()

> **المستودع الرسمي:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **شبكة التوزيع (jsDelivr CDN):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/`  
> **الرابط المباشر (Raw GitHub):** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/`  

---

## 📖 مقدمة عامة | General Introduction

### 🇸🇦 بالعربية
السلام عليكم.. هلق شو شغلة هالمستودع؟  
فيك تقول هذا وقف تقني ومستودع عام ومتاح للاستخدام غير التجاري (CC BY-NC 4.0)، عملناه لنوفر لكل مطور ومهندس برمجيات حابب يبني تطبيق إسلامي بيانات مرتبة ومناهج تفاعلية بنظام الحفظ والتعلم المصغر (Micro-learning)؛ من تحفيظ القرآن الكريم بالرسم العثماني، للفقه الشافعي الميسر، لأحكام ومخارج التجويد، وللسيرة النبوية مرتبة زمنياً.

فيك تسحب أي ملف وتستدعي البيانات بتطبيقك أو موقعك فوراً عبر الـ CDN أو روابط GitHub المباشرة، بدون ما توجع راسك بسيرفرات باك إند للبيانات الثابتة. وطبعاً متل ما وضحتلك، ملفات الـ JSON هون هي الأساس ومدققة ومجربة وبتعتمد عليها تطبيقاتنا، أما ملفات التوجيه والـ md فموجودة لتاخد منها الفكرة وتوظف الـ AI بمشروعك بطريقتك وبلا وجع راس.

### 🇬🇧 In English
Welcome to the **Open Islamic Tech Architecture & Datasets Ecosystem (Digital Waqf)**.  
This open repository serves as a Digital Waqf providing structured educational datasets for Islamic and Quranic application developers. Built with micro-learning principles, the datasets encompass Quranic micro-memorization in Uthmanic script, simplified Fiqh, Tajweed phonetics, and chronological Prophetic Seerah.

Developers can consume these datasets directly in mobile and web applications via CDN or direct raw endpoints.

---

## 🗂️ خريطة المناهج والبيانات المتاحة | Curriculum Catalog

| المسار (Path) | الوصف بالعربية | English Description | رابط الفهرس (Manifest) | الدليل الكامل (Guide) |
|---|---|---|---|---|
| [`/tajweed`](./tajweed/) | **10 أبواب و 50 ملف JSON** لأحكام ومخارج وصفات التجويد | 10 modules (50 files) covering phonetics, makharij, and rules | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/manifest.json) | [دليل التجويد](./tajweed/README.md) |
| [`/fiqh`](./fiqh/) | **أحكام الطهارة والصلاة والصيام** (معتمدة على المذهب الشافعي حالياً) | Fiqh dataset covering Taharah, Salah, and Sawm (Shafi'i madhhab) | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/manifest.json) | [دليل الفقه](./fiqh/README.md) |
| [/quran_oasis](./quran_oasis/) | **عقد قرآنية للحفظ المصغر** بالرسم العثماني (30 جزءاً، 114 سورة كاملة) | Complete 30-Juz bite-sized Quran memorization nodes | [manifest.json](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/manifest.json) | [دليل القرآن](./quran_oasis/README.md) |
| [`/quran/hafs`](./quran/hafs/) | **القرآن كاملاً برواية حفص عن عاصم** (نصوص، مضلعات إحداثيات 604 صفحة) | Complete Quran text & 604 page coordinate polygons (Hafs) | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran/hafs/manifest.json) | [دليل المصحف](./quran/README.md) |
| [`/quran/warsh`](./quran/warsh/) | **القرآن كاملاً برواية ورش عن نافع** (نصوص، مضلعات إحداثيات 604 صفحة) | Complete Quran text & 604 page coordinate polygons (Warsh) | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran/warsh/manifest.json) | [دليل المصحف](./quran/README.md) |
| [`/AlSera_Alnabaoia`](./AlSera_Alnabaoia/) | **8 أبواب زمنية تضم 59 درساً** لأحداث السيرة النبوية مرتبة تاريخياً | Chronological Seerah curriculum containing 59 interactive lessons | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/manifest.json) | [دليل السيرة](./AlSera_Alnabaoia/README.md) |
| [`/ALnawoi`](./ALnawoi/) | **أحاديث الأربعين النووية** مع سلاسل الأسانيد والفوائد الفقهية والتخريج | Imam Al-Nawawi's Hadiths with transmission chains & Fiqh points | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/manifest.json) | [دليل الحديث](./ALnawoi/README.md) |
| [`/seerah_map`](./seerah_map/) | **خريطة السيرة النبوية الجغرافية** مع إحداثيات GPS والربط القرآني | Geospatial Prophetic Seerah map with GPS coordinates | [`manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/manifest.json) | [دليل الخريطة](./seerah_map/README.md) |

---

## ⚡ شلون بتستدعي البيانات بمشروعك؟ | How to Consume the Data

### 1. عبر الروابط المباشرة (Instant Endpoints)

* **رابط الـ CDN (jsDelivr):**
  ```http
  https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@{VERSION}/{DIRECTORY}/{PATH_TO_JSON}
  ```
  > 💡 **نصيحة للمطورين:** بتطبيقات الإنتاج (Production) بننصحك تستخدم الإصدار الثابت `@v1.1.0` بدل `@main` مشان تضمن استقرار الكاش وتتجنب أي تغييرات مفاجئة بهيكل البيانات.
* **رابط GitHub الخام (Raw GitHub):**
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/{DIRECTORY}/{PATH_TO_JSON}
  ```

---

## 💻 أكواد الاستدعاء التوضيحية | Integration Snippets

### 📱 1. في تطبيقات Flutter / Dart
```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class IslamicDataService {
  static const String cdnBase = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main';

  /// استدعاء فهرس أي مسار ديناميكياً (tajweed / fiqh / quran_oasis / AlSera_Alnabaoia)
  static Future<Map<String, dynamic>> fetchManifest(String track) async {
    final response = await http.get(Uri.parse('$cdnBase/$track/manifest.json'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load $track manifest');
  }

  /// استدعاء أي درس JSON محدد
  static Future<Map<String, dynamic>> fetchLesson(String path) async {
    final response = await http.get(Uri.parse('$cdnBase/$path'));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load lesson from $path');
  }
}

// مثال عملي للاستخدام:
void loadSample() async {
  final lesson = await IslamicDataService.fetchLesson(
    'tajweed/03_Nun_Sakinah_and_Tanween/01_izhar_halqi.json'
  );
  print('عنوان المفهوم: ${lesson['steps'][0]['title']}');
}
```

---

### 🌐 2. في تطبيقات الويب (JavaScript / TypeScript / React / Next.js / Vue)
```typescript
const CDN_BASE = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main';

// دالة عامة لجلب البيانات
export async function getIslamicCurriculum(filePath: string) {
  try {
    const response = await fetch(`${CDN_BASE}/${filePath}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch dataset:', error);
    throw error;
  }
}

// مثال: جلب درس الطهارة الأول
getIslamicCurriculum('fiqh/01_Taharah/01_water_and_purity.json')
  .then(data => console.log('Loaded Steps Count:', data.steps.length));
```

---

### 🐍 3. في لغة بايثون (Python Backend / Data Processing)
```python
import requests

CDN_BASE = "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main"

def fetch_json(file_path: str) -> dict:
    url = f"{CDN_BASE}/{file_path}"
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = 'utf-8'
    return response.json()

# مثال: جلب عقدة من جزء عم
node = fetch_json("quran_oasis/juz_30/node_078_01.json")
print(f"Surah ID: {node['surahId']} - Title: {node['title']}")
print(f"Activities: {len(node['activities'])}")
```

---

### 📟 4. عبر أوامر cURL (Terminal / Testing)
```bash
# Fetch Tajweed Manifest
curl -s "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/manifest.json"

# Fetch Seerah Chapter 1
curl -s "https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/01_makka_w_wlada_alrasul.json"
```

---

## 🎧 التلاوات آية بآية | Verse-by-Verse Recitations

ملف [`audio/ayah_reciters.json`](./audio/ayah_reciters.json) فيه 44 مصحف آية بآية (حفص وورش) و5 ترجمات صوتية، كلها على سيرفر HEQ:

```http
https://heq-cdn.b-cdn.net/quran/{reciter}/{type}/{surah:03d}/{ayah:03d}.mp3
```

مثال آية الكرسي بصوت الحصري: `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/255.mp3`

---

## 🤖 مهارة Claude Code لبناء تطبيق إسلامي | Claude Code Skill

المستودع فيه مهارة جاهزة اسمها `heq-app-builder`. بتخلي Claude Code يبني تطبيق أو موقع إسلامي كامل من بيانات هالمستودع، وبيلتزم بالقواعد الشرعية وشروط الرخصة.
The repo ships a Claude Code skill, `heq-app-builder`, that builds a complete Islamic app or website from these datasets.

**التثبيت | Install** (داخل Claude Code):

```
/plugin marketplace add HuzhaifaEqbal/HEQ-Werdk-Open
/plugin install heq-app-builder@heq-werdk-open
```

وبعدها قلّه بس: «ابنيلي تطبيق إسلامي». | Then just ask: "Build me an Islamic app."

الملفات: [`skills/heq-app-builder/SKILL.md`](./skills/heq-app-builder/SKILL.md) (English) — [`SKILL.ar.md`](./skills/heq-app-builder/SKILL.ar.md) (العربية).

---

## 🛡️ المبادئ والضوابط المتبعة | Core Principles

1. **حظر بعثرة القرآن الكريم (Strictly No Scrambled Verses):** التزاماً بقدسية كلام الله عز وجل، لا تحتوي الأنشطة القرآنية على أي خلط أو بعثرة للآيات، بل تعتمد على الحفظ بالتكرار، ملء الفراغات الموضعية، ومعرفة الآية التالية.
2. **الاعتماد المذهبي في الفقه:** المحتوى الفقهي المتوفر حالياً في المستودع مبني وفق معتمد المذهب الشافعي مع توثيق المسائل من كتب المذهب المعتمدة (متن أبي شجاع، فتح القريب، كفاية الأخيار).
3. **التوثيق التاريخي في السيرة:** التسلسل الزمني للأحداث مبني وفق المشهور والمحقق في مصادر السيرة النبوية (الرحيق المختوم، سيرة ابن هشام).

---

## 📄 الترخيص وحقوق الاستخدام | License & Rights

هذا المستودع مرخص بموجب رخصة المشاع الإبداعي: **نسب المصنف - غير تجاري 4.0 دولي (CC BY-NC 4.0)**.  
المشروع متاح كوقف تقني عام ومتاح للاستخدام غير التجاري (CC BY-NC 4.0) لأغراض التعلم والتطوير غير الربحي لخدمة المحتوى الإسلامي والقرآني. الاستخدام التجاري المباشر غير مصرح به بدون إذن مسبق.  
للاطلاع على تفاصيل الترخيص، راجع ملف [LICENSE](./LICENSE)، ولتفاصيل مصادر البيانات ونسبها راجع [ATTRIBUTION.md](./ATTRIBUTION.md).
يخضع مجلد scripts/ لرخصة MIT (انظر scripts/LICENSE)، بينما البيانات والمحتوى التعليمي يخضعان لرخصة المشاع الإبداعي CC BY-NC 4.0.
للاستخدام التجاري، تواصل معنا للحصول على إذن مكتوب: developers@heqwerdk.com

الصور الموجودة في images/reciters/ وwallper/ وأي صور مجمّعة من الإنترنت جُمعت من مصادر متاحة على الإنترنت وأُجريت عليها تعديلات من فريق HEQ Werdk. حقوق الصور الأصلية تعود لأصحابها، ولا تشملها رخصة CC BY-NC 4.0 الخاصة بالمستودع. إن كنت صاحب حق وترغب بإزالة صورة، راسلنا على info@heqwerdk.com وسنزيلها فوراً.

---

*Waqf initiative for Islamic tech development and open educational resources.*
