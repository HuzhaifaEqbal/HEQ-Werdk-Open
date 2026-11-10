# 🌐 دليل وروابط استدعاء البيانات الإسلامية المتاحة للاستخدام غير التجاري (CC BY-NC 4.0) للمطورين
## (Open Islamic Data Integration Guide & Prompt for Developers & AI Models)

> ### 📌 اسمع يا صاحبي.. شو فكرة هالملف؟
> * **فهرس الـ API وروابط الـ CDN المباشرة:** عملتلك هاد الدليل لتسحب ملفات الـ JSON والبيانات الإسلامية فوراً بدون ما تضطر تحمل المستودع كله لعندك.
> * **استدعاء مباشر وسريع:** الروابط شغالة عبر شبكة jsDelivr العالمية، مفتوحة بـ CORS افتراضي، يعني بتشتغل معك بـ Flutter أو React أو أي Web Framework مباشرة وبلا وجع راس.
> * **نماذج كود جاهزة:** ضفتلك أمثلة كود سريعة تاخدها نسخ ولصق لتبني تطبيقك بأقل وقت ممكن.

---

> ### 🤖 برومبت جاهز إذا بدك تخلّي الذكاء الاصطناعي يبنيلك الكود (Master AI Prompt):
> **انسخ هاد البرومبت وعطيه للموديل تبعك (Claude / GPT / Gemini):**
> ```text
> اسمع، بدي منك تبني واجهة مستخدم أو تطبيق (Web / Mobile App) يستهلك البيانات والمناهج الإسلامية الموثقة بهاد الدليل.
> 
> الشغلات المطلوبة منك بالضبط:
> 1. بنية التطبيق: أنشئ Service أو ملف استدعاء لجلب ملفات المانيفست `manifest.json` بالأول، مشان تبني القوائم والتصنيفات ديناميكياً بدون هاردكودينغ.
> 2. روابط الـ CDN: استخدم روابط الـ CDN المباشرة الموضحة بالجداول تحت لكل مسار (تجويد، فقه، سيرة، أربعين نووية، واحة القرآن).
> 3. الكاش والترميز: فعّل Caching محلي للبيانات مشان ما تضل تسحب من السيرفر على الفاضي، واقرأ النصوص بترميز UTF-8 مشان الحركات والخطوط القرآنية تضل مضبوطة.
> 4. ابدأ هلق ببناء هيكل الـ Service والكود مباشرة بدون حشو ومقدمات طويلة.
> ```

---

> 💡 **ملاحظة للمطورين:** هاد الملف فيه كل الروابط المباشرة لملفات الـ JSON والأصول، يعني بتستدعيها فوراً بتطبيقك وموقعك بدون ما تضطر تدخل على GitHub أساساً.

## 📌 الصيغة القياسية للروابط (URL Pattern)

```text
https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@{VERSION}/{DIRECTORY}/{FILE_PATH}
```

* **المستودع الأساسي:** `HuzhaifaEqbal/HEQ-Werdk-Open`
* **الإصدار والنسخ (Version Tagging):**
  - **للإنتاج (Production):** بننصحك بشدة تستخدم Tag النسخة الثابتة مثل `@v1.0.0` بدل `@main`. ليش؟ مشان تضمن استقرار الكاش بشبكة jsDelivr وما يعلق معك كاش قديم، ولحتى إذا عدلنا هيكل ملفات الـ JSON بالمستقبل ما تضرب التطبيقات الشغالة بالمتاجر عند المستخدمين (تجنب الـ Breaking Changes).
  - **للتطوير والتجارب (Development):** فيك تستخدم `@main` عادي مشان تسحب آخر التحديثات والتعديلات فوراً.
* **بروتوكول الاستدعاء:** `HTTPS GET`
* **نوع الاستجابة:** `application/json` (أو صيغ الوسائط للصور والخطوط)

> 💡 **ملاحظة بخصوص تسمية المجلدات (Naming Conventions):**
> المجلدات الحالية معتمدة ومربوطة بالتطبيقات الموجودة مشان ما نكسر الروابط. لكن للمسارات الجديدة القادمة (مثل كتب الحديث الشريف، المتجهات، ومصادر التفسير) رح نعتمد نمط موحد كلياً بأحرف صغيرة `lowercase snake_case` (مثل: `/bukhari`، `/muslim`، `/daif_hadiths`) لحماية الروابط وتجنب مشاكل حساسية الأحرف (Case-Sensitivity) بسيرفرات اللينكس وأجهزة الأندرويد.

---

## 🗂️ 1. فهارس المانيفست الديناميكية (Master Manifests)

> **💡 أفضل ممارسة للموقع:** بدلاً من كتابة روابط جميع الدروس يدوياً، يمكن للموقع استدعاء ملف `manifest.json` مرة واحدة لبناء القوائم والتصنيفات ديناميكياً ثم جلب ملف الدرس المختار.

| المسار التعليمي | رابط المانيفست (jsDelivr CDN) | الغرض والاستخدام |
| :--- | :--- | :--- |
| **أحكام التجويد** | [`tajweed/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/manifest.json) | فهرس 10 أبواب و 50 درساً تفاعلياً مع مستويات الصعوبة والـ XP |
| **الفقه الشافعي** | [`fiqh/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/manifest.json) | شجرة الفقه (الطهارة، الصلاة، الصيام) مع مستوياتها وأسئلتها |
| **واحة القرآن (الحفظ المصغر)** | [`quran_oasis/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/manifest.json) | فهرس أجزاء عمّ (108 ملفات: 107 عقد حفظ + 1 تحدي صوتي)، تبارك، والفاتحة بدون أي خلط |
| **السيرة النبوية التفاعلية** | [`AlSera_Alnabaoia/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/manifest.json) | التسلسل الزمني لـ 8 حقب من المولد الشريف حتى الوفاة |
| **الأربعين النووية** | [`ALnawoi/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/manifest.json) | فهرس الأحاديث الأربعين المعتمدة (الحديثان 41 و42 قيد المراجعة) مع روابط الدفعات والأسانيد والتخريج |
| **خريطة السيرة الجغرافية** | [`seerah_map/manifest.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/manifest.json) | فهرس أحداث السيرة مع إحداثيات GPS وروابط الآيات |
| **المصحف الشريف (رواية حفص)** | [`quran/hafs/manifest.json`](https://heq-cdn.b-cdn.net/mushaf/hafs/manifest.json) | فهرس الـ 114 سورة كاملاً مع إحداثيات تتبع الآيات لـ 604 صفحات |
| **المصحف الشريف (رواية ورش)** | [`quran/warsh/manifest.json`](https://heq-cdn.b-cdn.net/mushaf/warsh/manifest.json) | فهرس رواية ورش (العد المدني) المعتمد من مجمع الملك فهد مع إحداثيات الـ 604 صفحات |

---

## 📖 2. روابط البيانات المباشرة حسب المسار (Direct Endpoints)

---

### 🟢 أولاً: مسار الأربعين النووية (`/ALnawoi`)

| الملف | الرابط المباشر (jsDelivr CDN) | وصف المحتوى ووظيفته |
| :--- | :--- | :--- |
| **المتون المكتملة (40 حديثاً)** | [`nawawi_40_complete.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_complete.json) | يحتوي على الأحاديث الأربعين المعتمدة في هذا الإصدار مع المتن، السند، التخريج، والمفردات في مصفوفة JSON واحدة (قيد الدراسة استكمال الحديثين 41 و42) |
| **الدفعة 1 (الأحاديث 1 - 10)** | [`nawawi_40_batch_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_01.json) | أحاديث النية، أركان الإسلام والإيمان، النهي عن الابتداع، الحلال والحرام، النصيحة |
| **الدفعة 2 (الأحاديث 11 - 20)** | [`nawawi_40_batch_02.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_02.json) | الورع والشك، ترك ما لا يعني، حب الخير للمؤمنين، حرمة دم المسلم، إكرام الجار، الحياء |
| **الدفعة 3 (الأحاديث 21 - 30)** | [`nawawi_40_batch_03.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_03.json) | الاستقامة، أبواب الخير والصدقة، كف اللسان، حدود الله وفرائضه |
| **الدفعة 4 (الأحاديث 31 - 40)** | [`nawawi_40_batch_04.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/ALnawoi/nawawi_40_batch_04.json) | الزهد، لا ضرر ولا ضرار، البينة على المدعي، تغيير المنكر، فضل الذكر ومغفرة الذنوب |

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل بيانات الحديث (JSON Schema Sample)</b></summary>

```json
[
  {
    "hadithId": "nawawi_40_01",
    "number": 1,
    "title": "إنما الأعمال بالنيات",
    "matn": "إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى...",
    "primarySahabi": "عمر بن الخطاب رضي الله عنه",
    "takhrij": "أخرجه البخاري (1) ومسلم (1907)",
    "authenticity": "صحيح متفق عليه",
    "isnadChain": [
      {
        "step": 1,
        "name": "عبد الله بن الزبير الحميدي",
        "grade": "ثقة حافظ",
        "generation": "أتباع التابعين"
      }
    ],
    "vocabulary": [
      {
        "word": "بِالنِّيَّاتِ",
        "meaning": "قصد الشيء مقترناً بفعله، ومحلها القلب"
      }
    ],
    "explanationPoints": [
      "النية شرط لصحة الأعمال وقبولها عند الله تعالى."
    ],
    "lessonsLearned": [
      "إخلاص العمل لله تعالى وتجريده من الرياء."
    ]
  }
]
```
</details>

---

### 🗺️ ثانياً: مسار خريطة السيرة الجغرافية المكانية (`/seerah_map`)

| الملف | الرابط المباشر (jsDelivr CDN) | وصف المحتوى ووظيفته |
| :--- | :--- | :--- |
| **أحداث وغزوات السيرة (الدفعة 1)** | [`seerah_major_events_batch_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/seerah_map/seerah_major_events_batch_01.json) | نقاط جغرافية مجهزة بـ `latitude` و `longitude` لغزوة بدر، أحد، الخندق، صلح الحديبية، وفتح مكة لعرضها على خرائط Mapbox / Leaflet / Google Maps |

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل بيانات الحدث الجغرافي (JSON Schema Sample)</b></summary>

```json
[
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
    "summary": "خرج المسلمون في الأصل لاعتراض قافلة قريش، ثم واجهوا جيشاً قريشياً بعد نجاة القافلة...",
    "quranicConnections": [
      {
        "surahNumber": 8,
        "surahName": "الأنفال",
        "ayahStart": 5,
        "ayahEnd": 19,
        "context": "تتناول خروج المؤمنين للقاء العدو، ودعاءهم وإمدادهم وتأييدهم في بدر."
      }
    ]
  }
]
```
</details>

---

### 🕌 ثالثاً: مسار السيرة النبوية الشريفة (`/AlSera_Alnabaoia`)

| الحقبة الزمنية | الرابط المباشر (jsDelivr CDN) | وصف المحتوى ووظيفته |
| :--- | :--- | :--- |
| **1. المولد والنشأة بمكة** | [`era_01_pre_islamic_and_birth.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/01_makka_w_wlada_alrasul.json) | أحوال جزيرة العرب قبل الإسلام، عام الفيل، رضاعته ﷺ، وكفالة جده وعمه |
| **2. الوحي والدعوة المكية** | [`era_02_dawah_in_makkah.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/02_alwahy_waldawa_fi_makka.json) | نزول الوحي في غار حراء، الدعوة السرية والجهرية، وصبر الصحابة |
| **3. التمهيد للهجرة** | [`era_03_altamhid_lilhijra.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/03_altamhid_lilhijra.json) | رحلة الطائف، الإسراء والمعراج، وبيعتي العقبة الأولى والثانية |
| **4. الهجرة وبناء المدينة** | [`era_04_alhijra_wbina_almadina.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/04_alhijra_wbina_almadina.json) | الهجرة النبوية، بناء المسجد النبوي، والمؤاخاة بين المهاجرين والأنصار |
| **5. الدفاع وبناء الدولة** | [`era_05_tathbit_almujtama.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/05_tathbit_almujtama_waldifaa.json) | معارك الدفاع عن المجتمع الإسلامي والتشريعات المدنية |
| **6. اتساع الدعوة وفتح مكة** | [`era_06_ittisaa_aldawa.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/06_ittisaa_aldawa_wfath_makka.json) | مكاتبة الملوك، صلح الحديبية، فتح مكة الأعظم، وتطهير الكعبة |
| **7. حجة الوداع والوفود** | [`era_07_hajjat_alwadaa.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/07_hajjat_alwadaa_walwufud.json) | عام الوفود، خطبة حجة الوداع، وتقرير حقوق الإنسان في الإسلام |
| **8. الرفيق الأعلى وأثر الرسالة** | [`era_08_akhir_hayat_alrasul.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/AlSera_Alnabaoia/08_akhir_hayat_alrasul_wathar_alrisala.json) | مرض النبي ﷺ ووفاته، وصاياه الأخيرة، وخلود الأثر الرسالي |

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل درس السيرة التفاعلي (JSON Schema Sample)</b></summary>

```json
[
  {
    "lesson_id": "01_makka_quraysh",
    "title": "مكة وقريش قبل البعثة",
    "steps": [
      {
        "type": "concept",
        "title": "مكة والبيت الحرام",
        "content": "كانت مكة موطن البيت الحرام، وإليه يقصد الناس للحج...",
        "sources": [
          {
            "book": "السيرة النبوية لابن هشام",
            "link": "https://islamweb.net/ar/library/content/58/0/"
          }
        ]
      },
      {
        "type": "question",
        "question_type": "multiple_choice",
        "question_text": "ما أبرز ما أكسب مكة مكانتها الدينية عند العرب؟",
        "options": ["وجود البيت الحرام", "كونها عاصمة للروم", "وقوعها على نهر كبير"],
        "correct_answer_index": 0,
        "explanation": "ارتبطت مكانة مكة بالبيت الحرام والحج إليه."
      }
    ]
  }
]
```
</details>

---

### ⚖️ رابعاً: مسار الفقه الشافعي الميسر (`/fiqh`)

#### 1. قسم الطهارة (`fiqh/01_Taharah`)
| الدرس | الرابط المباشر (jsDelivr CDN) | المحتوى |
| :--- | :--- | :--- |
| **أنواع المياه وأحكامها** | [`01_water_and_purity.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/01_water_and_purity.json) | الماء المطلق، المستعمل، النجس، والمتغير |
| **فروض الوضوء وسننه** | [`02_wudu_fard_and_sunnah.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/02_wudu_fard_and_sunnah.json) | الأركان الستة للوضوء مع السنن الشافعية |
| **نواقض الوضوء** | [`03_nullifiers_of_wudu.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/03_nullifiers_of_wudu.json) | خروج الخارج، زوال العقل، مس الفرج، لمس البشرة |
| **الغسل وموجباته** | [`04_ghusl_and_major_purification.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/04_ghusl_and_major_purification.json) | موجبات الغسل الأكبر وفروضه وكيفيته |
| **التيمم والمسح** | [`05_tayammum_and_wiping.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/05_tayammum_and_wiping.json) | شروط التيمم، المسح على الخفين والجبيرة |
| **اختبار التحدي للطهارة** | [`06_boss_level_taharah.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/01_Taharah/06_boss_level_taharah.json) | أسئلة نوازل وسيناريوهات فقهية مجمعة |

#### 2. قسم الصلاة (`fiqh/02_Salah`)
* **المستوى 1 (المواقيت، الشروط، الأركان، السنن، والمبطلات):**
  - مواقيت الصلوات الخمس والأذان: [`level_1/01_prayer_times_and_adhan.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/01_prayer_times_and_adhan.json)
  - شروط صحة الصلاة: [`level_1/02_conditions_of_prayer.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/02_conditions_of_prayer.json)
  - أركان الصلاة وسننها: [`level_1/03_pillars_and_sunnahs.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/03_pillars_and_sunnahs.json)
  - سنن الأبعاض والهيئات وسجود السهو: [`level_1/04_abd_hayat_and_sujood.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/04_abd_hayat_and_sujood.json)
  - مبطلات الصلاة ومكروهاتها: [`level_1/05_nullifiers_and_disliked_acts.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/05_nullifiers_and_disliked_acts.json)
  - اختبار المستوى الأول الشامل: [`level_1/06_boss_level_salah.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_1/06_boss_level_salah.json)
* **المستوى 2 (الجماعة، المسافر، الجمعة، الجنائز، والصلوات الخاصة):**
  - صلاة الجماعة والإمامة: [`level_2/01_congregational_prayer_and_imamate.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/01_congregational_prayer_and_imamate.json)
  - صلاة المسافر (القصر والجمع): [`level_2/02_traveler_prayer.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/02_traveler_prayer.json)
  - صلاة الجمعة وأحكامها: [`level_2/03_friday_prayer.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/03_friday_prayer.json)
  - الصلوات الخاصة (العيدين، الكسوف، والاستسقاء والجنائز): [`level_2/04_special_prayers_and_funerals.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/04_special_prayers_and_funerals.json)
  - سجدات السهو والتلاوة والشكر: [`level_2/05_prostrations_sahw_tilawah_shukr.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/05_prostrations_sahw_tilawah_shukr.json)
  - اختبار المستوى الثاني المتقدم: [`level_2/06_boss_level_salah_l2.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/02_Salah/level_2/06_boss_level_salah_l2.json)

#### 3. قسم الصيام (`fiqh/04_Sawm`)
* **المستوى 1 (الشروط، الرؤية، النية، الآداب والمفطرات):**
  - تعريف الصيام وشروطه: [`level_1/01_fasting_definition_and_conditions.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/01_fasting_definition_and_conditions.json)
  - ثبوت الشهر وليلة القدر: [`level_1/02_moon_sighting_and_laylat_al_qadr.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/02_moon_sighting_and_laylat_al_qadr.json)
  - أركان الصوم والنية والإمساك: [`level_1/03_fasting_intention_and_abstinence.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/03_fasting_intention_and_abstinence.json)
  - سنن الصيام وآدابه: [`level_1/04_fasting_sunnahs_and_etiquette.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/04_fasting_sunnahs_and_etiquette.json)
  - مفطرات الصوم ومكروهاته: [`level_1/05_fasting_invalidators_and_disliked_acts.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/05_fasting_invalidators_and_disliked_acts.json)
  - اختبار المستوى الأول للصيام: [`level_1/06_boss_level_sawm.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_1/06_boss_level_sawm.json)
* **المستوى 2 (الأعذار، الفدية، الكفارة، النوافل والاعتكاف):**
  - الأعذار المبيحة للفطر والفدية: [`level_2/01_fasting_excuses_and_redemption.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/01_fasting_excuses_and_redemption.json)
  - الكفارة الكبرى والإمساك لحرمة الوقت: [`level_2/02_fasting_expiation_and_holding_time.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/02_fasting_expiation_and_holding_time.json)
  - صوم التطوع والأيام المحرمة والمكروهة: [`level_2/03_fasting_voluntary_and_prohibited_days.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/03_fasting_voluntary_and_prohibited_days.json)
  - أحكام الاعتكاف وسننه ومبطلاته: [`level_2/04_fasting_i'tikaf_sunnah_and_invalidators.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/04_fasting_i'tikaf_sunnah_and_invalidators.json)
  - أحكام النذر والتتابع في الصوم: [`level_2/05_fasting_vows_and_continuity_rules.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/05_fasting_vows_and_continuity_rules.json)
  - اختبار الصيام المتقدم: [`level_2/06_boss_level_sawm_l2.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/06_boss_level_sawm_l2.json)
  - الملحق الإثرائي (المفاهيم الشائعة والمستحبات): [`level_2/fasting_enrichment_misconceptions.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/fiqh/04_Sawm/level_2/fasting_enrichment_misconceptions.json)

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل درس الفقه (JSON Schema Sample)</b></summary>

```json
{
  "steps": [
    {
      "type": "concept",
      "title": "أنواع المياه وحكم كل نوع",
      "content": "تنقسم المياه في الفقه الشافعي إلى أربعة أقسام رئيسية...",
      "example": "الماء الذي يُجمع من المطر أو مياه العيون والآبار يُعد ماءً مطلقاً طاهراً مطهراً...",
      "sources": [
        {
          "book": "متن أبي شجاع (غاية الاختصار)",
          "link": "https://shamela.ws/book/9780/1"
        }
      ]
    },
    {
      "type": "question",
      "question_type": "scenario_based",
      "scenario_text": "توضأ أحمد بماء وُضع فيه زعفران وورد كثير فتغير لونه ورائحته...",
      "question_text": "ما حكم صحة طهارة أحمد ووضوئه بهذا الماء في المذهب الشافعي؟",
      "options": ["طاهر مطهر يصح به الوضوء", "طاهر غير مطهر لا يصح به الوضوء", "نجس لا يجوز استعماله"],
      "correct_answer_index": 1,
      "explanation": "إذا تغير الماء تغيراً كثيراً بطاهر خالطه استغنى الماء عنه سُلب طهوريته."
    }
  ]
}
```
</details>

---

### 🎙️ خامساً: مسار أحكام التجويد (`/tajweed`)

يحتوي على 10 أبواب، كل باب يتألف من 5 دروس تفاعلية:

| الباب التعليمي | رابط الدرس الأول (نموذج) | رابط درس التحدي (Boss Level) |
| :--- | :--- | :--- |
| **1. المبادئ والمخارج** | [`01_intro_and_importance.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/01_Basics_and_Makharij/01_intro_and_importance.json) | [`05_boss_level_makharij.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/01_Basics_and_Makharij/05_boss_level_makharij.json) |
| **2. صفات الحروف** | [`01_sifat_intro.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/02_Sifat_Al_Huroof/01_sifat_intro.json) | [`05_boss_level_sifat.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/02_Sifat_Al_Huroof/05_boss_level_sifat.json) |
| **3. النون الساكنة والتنوين** | [`01_izhar_halqi.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/03_Nun_Sakinah_and_Tanween/01_izhar_halqi.json) | [`05_boss_level_nun.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/03_Nun_Sakinah_and_Tanween/05_boss_level_nun.json) |
| **4. الميم الساكنة والمشددة** | [`01_ikhfa_shafawi.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/04_Meem_Sakinah_and_Mushaddadah/01_ikhfa_shafawi.json) | [`05_boss_level_meem.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/04_Meem_Sakinah_and_Mushaddadah/05_boss_level_meem.json) |
| **5. المدود (الجزء الأول)** | [`01_madd_tabii.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/05_Madd_Rules_Part_1/01_madd_tabii.json) | [`05_boss_level_madd_1.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/05_Madd_Rules_Part_1/05_boss_level_madd_1.json) |
| **6. المدود (الجزء الثاني)** | [`01_madd_muttasil.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/06_Madd_Rules_Part_2/01_madd_muttasil.json) | [`05_boss_level_madd_2.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/06_Madd_Rules_Part_2/05_boss_level_madd_2.json) |
| **7. التفخيم والترقيق** | [`01_tafkheem_and_tarqeeq_basics.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/07_Tafkheem_and_Tarqeeq/01_tafkheem_and_tarqeeq_basics.json) | [`05_boss_level_tafkheem.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/07_Tafkheem_and_Tarqeeq/05_boss_level_tafkheem.json) |
| **8. علاقات الحروف** | [`01_mutamathilayn.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/08_Relations_Between_Letters/01_mutamathilayn.json) | [`05_boss_level_relations.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/08_Relations_Between_Letters/05_boss_level_relations.json) |
| **9. همزة الوصل والوقف** | [`01_hamzat_wasl_verbs.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/09_Hamzat_and_Waqf/01_hamzat_wasl_verbs.json) | [`05_boss_level_waqf.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/09_Hamzat_and_Waqf/05_boss_level_waqf.json) |
| **10. المقطوع والموصول والخاتمة** | [`01_maqtoo_and_mawsool_basics.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/10_Maqtoo_Mawsool_and_Conclusion/01_maqtoo_and_mawsool_basics.json) | [`05_boss_level_grand_finale.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/tajweed/10_Maqtoo_Mawsool_and_Conclusion/05_boss_level_grand_finale.json) |

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل درس التجويد (JSON Schema Sample)</b></summary>

```json
{
  "steps": [
    {
      "type": "concept",
      "title": "تعريف علم التجويد",
      "content": "التجويد اصطلاحاً هو إخراج كل حرف من مخرجه الدقيق، وإعطائه حقه ومستحقه...",
      "example": "قراءة (عَسَى) بدلاً من (عَصَى) هو تغيير المعنى، وليس تجويداً.",
      "audio_example": "https://heq-cdn.b-cdn.net/quran/al_husary/murattal/001/001.mp3"
    },
    {
      "type": "question",
      "question_type": "multiple_choice",
      "question_text": "ما هو التعريف الاصطلاحي لعلم التجويد عند علماء القراءات؟",
      "options": [
        "إخراج كل حرف من مخرجه مع إعطائه حقه ومستحقه من الصفات.",
        "تحسين الصوت بتلاوة القرآن الكريم ومحاكاة القراء المشهورين.",
        "معرفة معاني الكلمات الغريبة في القرآن لتسهيل الحفظ."
      ],
      "correct_answer_index": 0,
      "explanation": "التجويد اصطلاحاً هو إخراج كل حرف من مخرجه الدقيق مع إعطائه حقه ومستحقه."
    }
  ]
}
```
</details>

---

### 🌿 سادساً: مسار واحة القرآن والحفظ المصغر (`/quran_oasis`)

#### طريقة استخدام العقد القرآنية:
العقد الموجودة في هذا المستودع مبنية وفق خوارزميات المشروع، لذلك عدد العقد وطول كل عقدة مو ثابتين في جميع السور والدروس.

فينا نستخدم العقد الجاهزة كما هي، أو نعدّل طريقة تقسيمها حسب احتياجات التطبيق والخوارزمية المستخدمة. ويمكن استدعاء كل عقدة بشكل مستقل في Flutter أو أي إطار عمل آخر، بدل تحميل جميع العقد دفعة واحدة.

أما تفسير الآيات، فيمكن جلبه عند الحاجة من خلال API يختاره المطوّر، بدلاً من تخزين تفسير مكرر داخل ملفات العقد. في الأمثلة التوضيحية سنستخدم الاسم `your_API_ForTafseer` للدلالة على واجهة التفسير التي يحددها المطوّر؛ وهذا اسم بديل وليس API جاهزاً مقدّماً من المستودع.

* **سورة الفاتحة (الجزء 1):**
  - الآيات (1-7): [`juz_01/node_001_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_01/node_001_01.json)
* **سورة الملك (الجزء 29):**
  - المقطع الأول: [`juz_29/node_067_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_29/node_067_01.json)
* **جزء عمّ (الجزء 30 - 108 ملفات: 107 عقد حفظ + 1 تحدي صوتي):**
  - سورة النبأ (المقطع 1): [`juz_30/node_078_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_30/node_078_01.json)
  - سورة الإخلاص: [`juz_30/node_112_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_30/node_112_01.json)
  - سورة الفلق: [`juz_30/node_113_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_30/node_113_01.json)
  - سورة الناس: [`juz_30/node_114_01.json`](https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/quran_oasis/juz_30/node_114_01.json)

<details>
<summary><b>🔍 اضغط هون لعرض نموذج هيكل العقدة القرآنية (JSON Schema Sample)</b></summary>

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
      "options": ["أَحَدٌ", "وَاحِدٌ", "عَلِيمٌ", "قَدِيرٌ"]
    },
    {
      "activityId": "act_112_01_02",
      "type": "next_ayah",
      "currentAyahNumber": 1,
      "correctNextAyahNumber": 2,
      "wrongOptionsAyahNumbers": [3, 4]
    }
  ],
  "tutorContext": {
    "theme": "بيان صفة الله تعالى وتوحيده الخالص: الأحد الصمد المنزه عن الولد والوالد والمكافئ والمثيل"
  }
}
```
</details>

---

### 🟢 سابعاً: مسار المصحف الشريف وتتبع الآيات (`/quran` - حفص وورش)

> 🌟 **مرفوعة وموزعة سحابياً عبر سيرفر BunnyCDN المباشر (`heq-cdn.b-cdn.net`):**  
> لتفادي تضخيم مستودع GitHub بآلاف ملفات الفيكتور والصور، يتم استدعاء صفحات المصحف الـ 604 وإحداثيات تظليل وتتبع الآيات لورش وحفص مباشرة عبر سيرفر الـ CDN الرسمي.

| الأصل (Asset) | رابط استدعاء حفص عن عاصم | رابط استدعاء ورش عن نافع |
| :--- | :--- | :--- |
| **صفحة متجهة (Vector SVG)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/svg/{PAGE:03d}.svg` | `https://heq-cdn.b-cdn.net/mushaf/warsh/svg/{PAGE:03d}.svg` |
| **إحداثيات تتبع الآيات (JSON Polygons)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/coordinates/{PAGE:03d}.json` | `https://heq-cdn.b-cdn.net/mushaf/warsh/coordinates/{PAGE:03d}.json` |
| **نصوص السور والآيات (JSON)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/surahs/{SURAH:03d}.json` | `https://heq-cdn.b-cdn.net/mushaf/warsh/surahs/{SURAH:03d}.json` |
| **فهرس المصحف (Manifest)** | `https://heq-cdn.b-cdn.net/mushaf/hafs/manifest.json` | `https://heq-cdn.b-cdn.net/mushaf/warsh/manifest.json` |

<details>
<summary><b>🔍 اضغط لعرض نموذج مضلع تتبع الآية (Ayah Polygon Coordinate Sample)</b></summary>

```json
[
  {
    "ayahNumber": 1,
    "surahNumber": 1,
    "x": 66.48,
    "y": 34.46,
    "polygon": "181.08,18.31 57.54,18.31 57.54,48.94 181.08,48.94"
  }
]
```
</details>

---

## 🎨 3. مسار الوسائط والأصول البصرية (Media & UI Assets)

فيك تضمن الأيقونات والخطوط والخلفيات بموقعك أو تطبيقك مباشرة بالـ CSS أو بالـ `<img>` tags:

| نوع الأصل | الرابط القياسي المباشر |
| :--- | :--- |
| **الخطوط (Fonts)** | `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@{VERSION}/fonts/{FONT_NAME}.ttf` |
| **الأيقونات (Icons)** | `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@{VERSION}/icons/{ICON_NAME}.svg` |
| **الخلفيات (Wallpapers)** | `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@{VERSION}/wallper/{IMAGE_NAME}.jpg` |

> 🎙️ **ملاحظة هامة بخصوص الصوتيات:** ملفات الصوت مش مرفوعة على جيت هاب أساساً، رفعناها على سيرفر CDN خاص بمنصتنا مشان السرعة والحجم وما نثقل المستودع. رح نجهّزلك قريباً ملف عرض مستقل فيه كل روابط الصوتيات وأمثلة استدعائها بالتفصيل بس نخلص تجميعها. أو فيك تبحث عن "heqwerdk.com" وهناك بتلاقي تبويب خاص بال APIs كلها وفيه كمان روابط الاستدعائات الصوتية وفيه شوية أصول وفيه امثله للاستدعاء وفيك تختبر الرابط قبل متنسخ الاستدعاء

---

## 💻 4. نماذج أكواد جاهزة للربط والاستدعاء (Code Snippets for Web & Mobile)

### 1️⃣ جافاسكريبت نقية (Vanilla JavaScript / Fetch API)

```javascript
// دالة عامة لاستدعاء أي ملف من المستودع
async function fetchIslamicData(path) {
  const BASE_URL = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/';
  try {
    const response = await fetch(`${BASE_URL}${path}`);
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error('Failed to load dataset:', error);
    return null;
  }
}

// مثال: استدعاء متن الأربعين النووية كاملاً
fetchIslamicData('ALnawoi/nawawi_40_complete.json').then(data => {
  console.log(`تم تحميل ${data.length} حديث بنجاح!`);
  console.log('الحديث الأول:', data[0].matn);
});
```

---

### 2️⃣ رياكت / نيكست جي اس (React / Next.js Hook)

```tsx
import { useState, useEffect } from 'react';

export function useIslamicManifest(track: 'tajweed' | 'fiqh' | 'ALnawoi' | 'AlSera_Alnabaoia') {
  const [manifest, setManifest] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const url = `https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/${track}/manifest.json`;
    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        setManifest(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching manifest:', err);
        setLoading(false);
      });
  }, [track]);

  return { manifest, loading };
}
```

---

### 3️⃣ فلاتر / دارت (Flutter / Dart Service)

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class IslamicCdnService {
  static const String baseUrl = 'https://cdn.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main';

  static Future<Map<String, dynamic>?> getSeerahMapEvents() async {
    final uri = Uri.parse('$baseUrl/seerah_map/seerah_major_events_batch_01.json');
    final response = await http.get(uri);
    if (response.statusCode == 200) {
      return jsonDecode(utf8.decode(response.bodyBytes));
    }
    return null;
  }
}
```

---

## ⚡ 5. ملاحظات تقنية هامة للمطورين (Technical Notes for Developers)

1. **دعم الـ CORS:** جميع الروابط تدعم `Access-Control-Allow-Origin: *` افتراضياً، وتعمل عبر أي دومين.
2. **السرعة والكاش (Caching):** تقوم شبكة jsDelivr بتوزيع الملفات على مئات السيرفرات السحابية العالمية لتقليل زمن الاستجابة (Latency < 25ms).
3. **تحديث الكاش الفوري (Cache Purge):** عند رفع أي تحديث جديد إلى GitHub، يمكنك تفريغ كاش jsDelivr فوراً بطلب الرابط بالشكل:
   ```text
   https://purge.jsdelivr.net/gh/HuzhaifaEqbal/HEQ-Werdk-Open@main/{DIRECTORY}/{FILE_PATH}
   ```
4. **تجنب مشاكل تشفير الحروف العربية:** تأكد دائماً من قراءة الاستجابة بترميز `UTF-8` في تطبيقك حتى لا تظهر الحروف العربية كرموز مشوهة.
