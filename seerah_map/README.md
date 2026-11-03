# 🗺️ خريطة السيرة النبوية الجغرافية والتفاعلية — دليل المطور
## (Interactive Seerah Geospatial Map & Battles Dataset — Developer Guide)

> **Repository:** [https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open](https://github.com/HuzhaifaEqbal/HEQ-Werdk-Open)  
> **Direct Raw Endpoint:** `https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/seerah_map/`  
> **Global Fast CDN (jsDelivr):** `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/`  
> **Features:** Latitude/Longitude Coordinates, Quranic Connections, Timeline, Historical Summaries

---

## 🌍 نظرة عامة (Overview)

### 🇸🇦 بالعربية
بهاد المسار جمعنالك أحداث وغزوات السيرة النبوية مع بياناتها الجغرافية والمكانية.
كل حدث مربوط بإحداثياته (خط العرض وخط الطول `latitude / longitude`)، وتاريخه بالهجري، وملخص تاريخي عن الحدث، مع ربط مباشر بالآيات القرآنية اللي نزلت فيه، مشان تقدر تبني خريطة تفاعلية للسيرة بتطبيقك بـ (Flutter Mapbox أو Google Maps أو Leaflet) بسهولة وبلا تعقيد.

### 🇬🇧 In English
This dataset delivers a verified geospatial and chronological index of major historical events and battles from the Prophetic Seerah. Each event is anchored with GPS coordinates (`latitude`, `longitude`), historical dates (Hijri year, month, and day), participants, and direct thematic connections to relevant Quranic verses (`quranicConnections`), empowering developers to build rich interactive maps using Flutter Mapbox, Google Maps, or Leaflet.

---

## ⚡ روابط الاستدعاء المباشر (Direct Endpoints)

* **jsDelivr CDN:**
  ```http
  https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/seerah_major_events_batch_01.json
  ```
* **Raw GitHub:**
  ```http
  https://raw.githubusercontent.com/HuzhaifaEqbal/HEQ-Werdk-Open/main/seerah_map/seerah_major_events_batch_01.json
  ```
* **Dynamic Manifest:**
  ```http
  https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/manifest.json
  ```

---

## 📐 هيكل بيانات الحدث الجغرافي (JSON Event Schema)

```json
{
  "eventId": "seerah_001",
  "title": "غزوة بدر الكبرى (يوم الفرقان)",
  "period": "madani",
  "yearHijri": 2,
  "monthHijri": "رمضان",
  "dayHijri": 17,
  "location": {
    "name": "ميدان بدر",
    "modernRegion": "منطقة المدينة المنورة - محافظة بدر",
    "modernCountry": "SA",
    "latitude": 23.77227,
    "longitude": 38.78964
  },
  "summary": "خرج المسلمون لاعتراض قافلة قريش، ثم واجهوا جيشاً وانتهت المعركة بانتصار المسلمين...",
  "quranicConnections": [
    {
      "surahNumber": 8,
      "surahName": "الأنفال",
      "ayahStart": 5,
      "ayahEnd": 19,
      "context": "تتناول خروج المؤمنين للقاء العدو ودعاءهم وتأييدهم في بدر."
    }
  ]
}
```

---

## 💻 كود الاستدعاء والتكامل مع خرائط فلاتر (Flutter / Dart)

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class SeerahMapService {
  static const String endpoint = 
      'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/seerah_major_events_batch_01.json';

  static Future<List<dynamic>> fetchEvents() async {
    final response = await http.get(Uri.parse(endpoint));
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    throw Exception('Failed to load Seerah map events');
  }
}
```

---

هذا المحتوى مرخّص وفق رخصة CC BY-NC 4.0، باستثناء ما هو مذكور في ملف LICENSE (الخط، مواد الأطراف الأخرى، الهوية البصرية، الصور المجمّعة). التفاصيل في LICENSE وATTRIBUTION.md.
