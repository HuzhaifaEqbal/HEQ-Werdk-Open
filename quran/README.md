# 📖 منظومة بيانات القرآن الكريم وتتبع الآيات (حفص وورش)
## HEQ Werdk Quran Datasets, Coordinates & Page Artwork Guide

> **إصدار موثوق ومفحوص رقمياً:**  
> هذا الدليل والبيانات مبنية ومطابقة لمصاحف **مجمع الملك فهد لطباعة المصحف الشريف (KFGQPC)** بروايتي:
> 1. **حفص عن عاصم** (6236 آية - العد الكوفي).
> 2. **ورش عن نافع من طريق الأزرق** (6214 آية - العد المدني الأخير).

---

## 🗂️ هيكلة المجلدات (Repository Structure)

```text
quran/
├── hafs/                          # بيانات رواية حفص عن عاصم
│   ├── manifest.json              # فهرس الـ 114 سورة (أرقام، صفحات، عدد آيات)
│   ├── surahs/                    # 114 ملف JSON لكل سورة (001.json -> 114.json)
│   │   └── 001.json               # نص عثماني + نص إملائي للبحث + أرقام الآيات
│   └── coordinates/               # 604 ملف JSON لإحداثيات تتبع الآيات
│       └── 001.json -> 604.json   # مضلعات الآيات (Polygons) على الصفحة
│
├── warsh/                         # بيانات رواية ورش عن نافع
│   ├── manifest.json              # فهرس الـ 114 سورة بترقيم وضبط ورش
│   ├── surahs/                    # 114 ملف JSON لكل سورة (001.json -> 114.json)
│   │   └── 001.json               # نص عثماني معتمد لورش + أرقام الآيات
│   └── coordinates/               # 604 ملف JSON لإحداثيات تتبع آيات ورش
│       └── 001.json -> 604.json   # مضلعات الآيات (Polygons) لصفحات ورش
│
├── viewer.html                    # مستعرض ومصحح تفاعلي للمراجعة والتتبع
└── README.md                      # هذا الدليل التوضيحي
```

> 💡 **ملاحظة بخصوص صفحات الفيكتور (SVG):**  
> ملفات الـ SVG المتجهة لصفحات المصحف (1,208 صفحة لحفص وورش) مستضافة سحابياً عبر سيرفر الـ CDN الرسمي (`https://heq-cdn.b-cdn.net/mushaf/`) لتفادي تضخيم حجم مستودع Git، ويتم استدعاؤها في التطبيقات والمستعرض مباشرة عبر الروابط الموضحة أدناه.

---

## 📐 ما هي إحداثيات تتبع الآيات (Ayah Polygons)؟ وكيف تعمل؟

لكل صفحة من صفحات المصحف الـ 604، يوجد ملف JSON بمسار `coordinates/{page}.json`.  
يحتوي الملف على مصفوفة بكل الآيات الموجودة على تلك الصفحة مع مضلع الإحداثيات (`polygon`):

```json
[
  {
    "ayahNumber": 1,
    "surahNumber": 1,
    "x": 66.48,
    "y": 34.46,
    "polygon": "181.08,18.31 57.54,18.31 57.54,48.94 181.08,48.94"
  },
  {
    "ayahNumber": 2,
    "surahNumber": 1,
    "x": 66.5,
    "y": 64.9,
    "polygon": "195.43,49.25 43.19,49.25 43.19,79.88 195.43,79.88"
  }
]
```

### فوائد الإحداثيات للمطورين:
1. **التظليل التفاعلي مع الصوت (Audio-Sync Highlighting):** عند قراءة القارئ لآية معينة، يضيء التطبيق المضلع الخاص بالآية بلون ذهبي أو أخضر شفاف.
2. **الضغط لاختيار الآية (Click-to-Select):** عند نقر المستخدم على أي مكان بالصفحة، يكتشف التطبيق أي مضلع تم النقر داخله ويعرض التفسير أو يشغل التلاوة فوراً.

---

## ☁️ روابط الاستدعاء المباشرة عبر شبكة التوزيع العالمية (CDN Endpoints)

تتوفر صفحات المصحف المتجهة (Vector SVGs) وإحداثيات تتبع الآيات ونصوص السور متاحة للاستخدام غير التجاري (CC BY-NC 4.0) عبر سيرفر الـ CDN الرسمي التابع للمنصة:

| الأصل (Asset) | رابط استدعاء رواية حفص | رابط استدعاء رواية ورش |
|---|---|---|
| **صفحة متجهة (SVG)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/svg/{page}.svg` | `https://heq-cdn.b-cdn.net/mushaf/warsh/svg/{page}.svg` |
| **إحداثيات التتبع (JSON)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/coordinates/{page}.json` | `https://heq-cdn.b-cdn.net/mushaf/warsh/coordinates/{page}.json` |
| **نصوص السور (JSON)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/surahs/{surah}.json` | `https://heq-cdn.b-cdn.net/mushaf/warsh/surahs/{surah}.json` |

---

## 🖥️ المستعرض المحلي التفاعلي (`viewer.html`)

للتأكد والتدقيق ومراجعة الإحداثيات وتطابق الصفحات والآيات قبل الرفع:
1. افتح ملف `quran/viewer.html` مباشرة بأي متصفح (Chrome, Edge, Safari, Firefox).
2. اختر الرواية: **حفص** أو **ورش**.
3. اختر رقم السورة أو رقم الصفحة (1 - 604).
4. مرر الفأرة فوق أي آية لترى التظليل التلقائي مع عرض نص الآية بالرسم العثماني وبيانات الـ Polygon.

---

## 📱 مثال كود Flutter لرسم المضلع التفاعلي (Ayah Highlighter)

```dart
import 'package:flutter/material.dart';

class AyahPolygonPainter extends CustomPainter {
  final List<Offset> points;
  final Color highlightColor;

  AyahPolygonPainter({required this.points, this.highlightColor = const Color(0x5510B981)});

  @override
  void paint(Canvas canvas, Size size) {
    if (points.isEmpty) return;

    final paint = Paint()
      ..color = highlightColor
      ..style = PaintingStyle.fill;

    final borderPaint = Paint()
      ..color = const Color(0xFF10B981)
      ..strokeWidth = 2.0
      ..style = PaintingStyle.stroke;

    final path = Path();
    path.moveTo(points[0].dx, points[0].dy);
    for (int i = 1; i < points.length; i++) {
      path.lineTo(points[i].dx, points[i].dy);
    }
    path.close();

    canvas.drawPath(path, paint);
    canvas.drawPath(path, borderPaint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}
```
