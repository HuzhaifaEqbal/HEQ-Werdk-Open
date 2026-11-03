# 🗺️ خريطة وهيكل مسار الفقه والعبادات اليومية
## (Fiqh Curriculum Structure Map & Interactive Node Registry)

> ### 📌 الوظائف والمهام الأساسية لهذا الملف (File Functions & Scope):
> * **خريطة المجلدات والملفات الفقهية:** فهرسة العقد المكتملة (الطهارة، الصلاة بمستوييها، الصيام بمستوييه) والعقد المستقبلية (الزكاة والحج).
> * **توثيق الدروس والـ Boss Level:** تصنيف ملفات الدروس المتناوبة (`01` إلى `05`) وملفات التحدي الملكي (`06`).
> * **مخطط المنهج الشافعي المعتمد:** فهرس كل درس ومحتواه المعتمد وأدلته.
> * **الفئة المستهدفة:** مهندسو الواجهة الخلفية، مطورو التطبيقات، ومهندسو المحتوى الفقهي.

---

## 📁 المسار الجذري
```
heq_werdk_backend/data/fiqh/
```

---

## ⚖️ المذهب المعتمد
**المذهب الشافعي** — مع الإشارة للخلاف الفقهي المعتبر داخل حقل `content` عند الضرورة.

---

## 🏗️ البنية العامة للمجلدات

```
fiqh/
├── 01_Taharah/                 ← عقدة الطهارة (مكتملة ومحدثة تفاعلياً ✅)
├── 02_Salah/                   ← عقدة الصلاة (مكتملة ومحدثة تفاعلياً ✅) #كلاود
│   ├── level_1/                ← المستوى الأول (6 ملفات كاملة ✅)
│   └── level_2/                ← المستوى الثاني (6 ملفات كاملة ✅)
├── 03_Zakah/                   ← عقدة الزكاة (قيد التجهيز)
├── 04_Sawm/                    ← عقدة الصيام (مكتملة ومحدثة تفاعلياً بمستوييها ✅) #جيميني
│   ├── (المستوى الأول)         ← 6 ملفات كاملة (01→05 + Boss) ✅
│   └── level_2/                ← المستوى الثاني (6 ملفات كاملة + ملحق إثرائي) ✅
├── 05_Hajj/                    ← عقدة الحج والعمرة (قيد التوليد)
├── AGENT_HANDOFF_GUIDE.md      ← وثيقة تسليم واستكمال العمل للوكلاء الذكياء 📜
└── STRUCTURE_MAP.md
```

كل مجلد يحتوي على:
- `01_*.json` → `05_*.json` : دروس Micro-learning تفاعلية
- `06_boss_level_*.json` : اختبار ملكي شامل للعقدة

> ⚠️ **ملاحظة:** عدد ملفات الدروس قد يختلف بين العقدات حسب حجم المادة العلمية.
> عقدة الطهارة مثلاً: 5 دروس + boss واحد = 6 ملفات.

---

## 📐 هيكل ملفات الدروس (01 → 05)

> **نمط Micro-learning تفاعلي** — كل ملف = خطوات بالتناوب الإلزامي بين بطاقة شرح (`concept`) موثقة وبطاقة سؤال (`question`) بأحد الأنواع التفاعلية الأربعة.

### 1. بطاقة الشرح الموثقة (Concept)
```json
{
  "type": "concept",
  "title": "عنوان المفهوم (مثال: شروط الوضوء)",
  "content": "شرح علمي دقيق للمفهوم.",
  "example": "مثال عملي يقرب الفهم.",
  "image_url": "{{CDN_IMAGE_WUDU_CONDITIONS}}",
  "sources": [
    {
      "book": "متن أبي شجاع (غاية الاختصار)",
      "link": "https://shamela.ws/book/9780/1"
    }
  ]
}
```

### 2. أنواع بطاقات الأسئلة التفاعلية (Question Types)

#### أ) الخيارات المتعددة (Multiple Choice)
```json
{
  "type": "question",
  "question_type": "multiple_choice",
  "question_text": "ما حكم ...؟",
  "image_url": "{{CDN_IMAGE_OPTIONAL}}",
  "options": ["خيار 1", "خيار 2", "خيار 3", "خيار 4"],
  "correct_answer_index": 0,
  "explanation": "الشرح الفقهي المفصل لسبب صحة الإجابة."
}
```

#### ب) ملء الفراغات (Fill in the Blanks)
يُطلب من المستخدم سحب الكلمات وإسقاطها في الفراغات (يُمثل الفراغ بـ `___`).
```json
{
  "type": "question",
  "question_type": "fill_in_the_blanks",
  "question_text": "الماء القليل ينجس بمجرد ___ النجاسة، بينما الماء الكثير لا ينجس إلا بـ ___ أحد أوصافه.",
  "correct_words": ["ملاقاة", "تغير"],
  "distractors": ["انفصال", "ركود"],
  "explanation": "القاعدة الفقهية تقتضي تفرقة بين القليل والكثير بملاقاة النجاسة أو تغير الوصف."
}
```

#### ج) الكلمات المبعثرة / الترتيب (Scrambled Words / Ordering)
يُطلب من المستخدم ترتيب الأفعال أو الخطوات فقهياً بشكل منطقي وصحيح.
```json
{
  "type": "question",
  "question_type": "scrambled_words",
  "question_text": "رتب خطوات تطهير الإناء الذي ولغ فيه الكلب شرعاً بالمذهب الشافعي:",
  "correct_order": [
    "إراقة ما في الإناء وإزالة جرم النجاسة",
    "غسل الإناء ست غسلات بالماء الطهور",
    "غسله مرة سابعة ممزوجة بالتراب الطهور"
  ],
  "explanation": "يُطهر الإناء بسبع غسلات إحداهن بالتراب بعد إزالة عين النجاسة."
}
```

#### د) قصة أو سيناريو واقعي (Scenario Based)
قصة قصيرة تضع المستخدم في موقف عملي فقهي ثم تطرح سؤالاً استنتاجياً.
```json
{
  "type": "question",
  "question_type": "scenario_based",
  "scenario_text": "توضأ أحمد بماء وُضع فيه زعفران كثير، فتغير لونه ورائحته تغيراً تاماً بمخالط طاهر.",
  "question_text": "ما حكم صحة طهارة أحمد ووضوئه بهذا الماء في المذهب الشافعي؟",
  "options": [
    "الوضوء غير صحيح؛ لأن الماء صار طاهراً في نفسه غير مطهر لغيره",
    "الوضوء صحيح كلياً؛ لأن التغير كان بمادة طاهرة ومستطابة",
    "الوضوء صحيح مجزئ مع الكراهة التنزيهية",
    "الماء نجس كلياً ويحرم استخدامه"
  ],
  "correct_answer_index": 0,
  "explanation": "الماء المتغير بمخالط طاهر يستغني الماء عنه طاهر في نفسه غير مطهر لغيره."
}
```

---

### جدول الحقول الشامل:

| الحقل | النوع | خاص بـ | الوصف |
|-------|-------|--------|-------|
| `steps` | `Array` | الملف ككل | مصفوفة الخطوات التناوبية في الدرس |
| `type` | `"concept"` أو `"question"` | كلاهما | نوع الخطوة |
| `title` | `String` | concept | عنوان بطاقة الشرح |
| `content` | `String` | concept | الشرح الفقهي الدقيق (شافعي مع ذكر الخلاف إن وجد) |
| `example` | `String` | concept | مثال فقهي تطبيقي أو حالة واقعية |
| `image_url` | `String (URL/Token)` | concept / question | وسم صورة الـ CDN التوضيحية بصيغة `{{CDN_IMAGE_*}}` |
| `sources` | `Array[Object]` | concept | قائمة المراجع الفقهية الموثقة `[{"book": "...", "link": "..."}]` |
| `question_type` | `String` | question | أحد الأنواع: `multiple_choice` / `fill_in_the_blanks` / `scrambled_words` / `scenario_based` |
| `question_text` | `String` | question | نص السؤال أو المطلوب في التحدي |
| `scenario_text` | `String` | scenario_based | نص القصة أو الموقف العملي الفقهي |
| `options` | `Array[String]` | multiple_choice / scenario_based | قائمة الخيارات المتاحة للمستخدم |
| `correct_answer_index` | `Number (0..n)` | multiple_choice / scenario_based | فهرس الإجابة الصحيحة ضمن مصفوفة الخيارات |
| `correct_words` | `Array[String]` | fill_in_the_blanks | الكلمات الصحيحة التي تسقط في الفراغات الممثلة بـ `___` بالترتيب |
| `distractors` | `Array[String]` | fill_in_the_blanks | كلمات التمويه الإضافية غير الصحيحة |
| `correct_order` | `Array[String]` | scrambled_words | الترتيب الصحيح للخطوات أو الكلمات المبعثرة |
| `explanation` | `String` | question | الشرح الفقهي التوضيحي المفصل لسبب صحة الإجابة |

---

## 📐 هيكل ملفات Boss Level

> **اختبار ملكي شامل** — يغطي جميع دروس العقدة — يُقرأ كـ `Array` مباشر بدون كائن رئيسي.

```json
[
  {
    "id": "q1",
    "type": "multiple_choice",
    "question_text": "سؤال تطبيقي شامل يربط موضوعات العقدة",
    "image_url": "{{CDN_IMAGE_BOSS_WATER_CONTAMINATION}}",
    "options": ["خيار1", "خيار2", "خيار3", "خيار4"],
    "correct_answer_index": 0,
    "explanation": "شرح وافٍ يربط بين مواضيع العقدة ويؤصل الحكم الفقهي"
  }
]
```

> ⚠️ **تنبيه للمطور:**
> - ملفات الدروس (01→05): تُقرأ كـ `Object` له مفتاح `steps`
> - ملفات Boss: تُقرأ كـ `Array` مباشر — لا يوجد object رئيسي

---

## 📚 قائمة الملفات الكاملة

### 📂 01 — عقدة الطهارة ✅ مكتملة ومحدثة تفاعلياً 100%

| الملف | الموضوع | Steps | التنويع التفاعلي | النوع |
|-------|---------|-------|------------------|-------|
| `01_water_and_purity.json` | أنواع المياه وأحكام النجاسات والاستنجاء | 10 | Multiple Choice + Scenario + Fill in Blanks + Scrambled + توثيق | Micro-learning |
| `02_wudu_fard_and_sunnah.json` | فرائض الوضوء الستة وسننه | 10 | Multiple Choice + Scenario + Fill in Blanks + Scrambled + توثيق | Micro-learning |
| `03_nullifiers_of_wudu.json` | نواقض الوضوء الأربعة | 8 | Multiple Choice + Scenario + Fill in Blanks + Scrambled + توثيق | Micro-learning |
| `04_ghusl_and_major_purification.json` | موجبات الغسل وأركانه وسننه | 6 | Scenario + Fill in Blanks + Scrambled + توثيق | Micro-learning |
| `05_tayammum_and_wiping.json` | المسح على الخفين والتيمم | 6 | Scenario + Fill in Blanks + Scrambled + توثيق | Micro-learning |
| `06_boss_level_taharah.json` | 🏆 الاختبار الملكي — عقدة الطهارة | 5 أسئلة | Multiple Choice شامل مع صور CDN | Boss Level |

---

### 📂 02 — عقدة الصلاة ✅ مكتملة ومحدثة تفاعلياً 100% #كلاود

> **ملاحظة بنيوية:** عقدة الصلاة تحتوي على مجلد فرعي `level_1/` لأن المحتوى مقسم إلى مستويات.
> المسار: `fiqh/02_Salah/level_1/`

| الملف | الموضوع | Steps | التنويع التفاعلي | النوع |
|-------|---------|-------|------------------|-------|
| `01_prayer_times_and_adhan.json` | مواقيت الصلوات الخمس وأحكام الأذان والإقامة والقضاء | 11 | Multiple Choice + توثيق | Micro-learning |
| `02_conditions_of_prayer.json` | شروط صحة الصلاة (ستر العورة، طهارة الخبث، القبلة، دخول الوقت) | 11 | Multiple Choice + توثيق | Micro-learning |
| `03_pillars_and_sunnahs.json` | أركان الصلاة وسننها (القيام، النية، التكبير، الفاتحة، الركوع، السجود، الترتيب) | 12 | Multiple Choice + Matching + توثيق | Micro-learning |
| `04_abd_hayat_and_sujood.json` | سنن الأبعاض (التشهد الأول، القنوت) وسنن الهيئات وأحكام سجود السهو | 12 | Multiple Choice + Matching + توثيق | Micro-learning |
| `05_nullifiers_and_disliked_acts.json` | مبطلات الصلاة ومكروهاتها ومستحبات الخشوع ومكفرات الذنوب | 13 | Multiple Choice + Matching + توثيق | Micro-learning |
| `06_boss_level_salah.json` | 🏆 الامتحان الملكي الشامل — عقدة الصلاة (المستوى الأول) | 10 أسئلة | Multiple Choice + Matching شامل مع صور CDN | Boss Level |

#### أنواع الأسئلة المستخدمة في عقدة الصلاة:

| النوع | الوصف | عدد الاستخدامات |
|-------|-------|----------------|
| `multiple_choice` | خيارات متعددة كلاسيكية | الأغلبية |
| `matching` | مطابقة/توصيل بين عمودين (`pairs`) | 5 أسئلة في الدروس + 1 في Boss |

> ⚠️ **ملاحظة للمطور:** نوع `matching` غير مذكور في `GEMINI_DATA_STRUCTURING_GUIDE.md` الأصلي لكنه مُستخدم في البيانات الخام. الهيكل:
> ```json
> {
>   "type": "question",
>   "question_type": "matching",
>   "question_text": "صل كل ... بحكمه ...",
>   "pairs": [
>     { "item": "النص الأيسر", "match": "النص الأيمن المطابق" }
>   ],
>   "explanation": "..."
> }
> ```
> في ملف Boss Level، الـ `matching` يستخدم `"type": "matching"` مباشرة (بدون `question_type`).

#### التحويلات التي أُجريت على البيانات الخام:

| التحويل | التفاصيل |
|---------|----------|
| `fill_in_the_blank` → `multiple_choice` | الأسئلة الأصلية استخدمت `options` + `correct_answer_index` (بنية MC فعلياً) |
| `concept_illustration` → `concept` | تم تحويلها لبطاقات شرح عادية مع إضافة `sources` و `image_url` |
| إضافة `sources` | أُضيفت مراجع شافعية موثقة لكل بطاقة concept (متن أبي شجاع، فتح القريب، كفاية الأخيار، منهاج الطالبين) |
| إضافة `image_url` | أُضيفت وسوم CDN بصيغة `{{CDN_IMAGE_SALAH_*}}` |

---

### 📂 02 — عقدة الصلاة (المستوى الثاني) ✅ مكتملة ومحدثة تفاعلياً 100% #كلاود

> **المسار:** `fiqh/02_Salah/level_2/`
> يغطي المستوى الثاني موضوعات الصلاة المتقدمة (الجماعة، المسافر، الجمعة، الصلوات الخاصة، وسجود السهو والتلاوة والشكر).

| الملف | الموضوع | Steps | التنويع التفاعلي | النوع |
|-------|---------|-------|------------------|-------|
| `01_congregational_prayer_and_imamate.json` | صلاة الجماعة وشروط صحة الاقتداء والإمامة | 8 | Multiple Choice + Matching + توثيق | Micro-learning |
| `02_traveler_prayer.json` | صلاة المسافر (القصر والجمع وشروطهما وجمع المطر) | 8 | Multiple Choice + Matching + توثيق | Micro-learning |
| `03_friday_prayer.json` | صلاة الجمعة (شروطها، أركان الخطبتين، إدراك المسبوق) | 8 | Multiple Choice + Matching + توثيق | Micro-learning |
| `04_special_prayers_and_funerals.json` | صلاة العيدين والكسوف والاستسقاء والجنازة | 8 | Multiple Choice + Matching + توثيق | Micro-learning |
| `05_prostrations_sahw_tilawah_shukr.json` | أحكام سجود السهو وأسبابه، وسجود التلاوة، وسجود الشكر | 6 | Multiple Choice + Matching + توثيق | Micro-learning |
| `06_boss_level_salah_l2.json` | 🏆 الامتحان الملكي الشامل — عقدة الصلاة (المستوى الثاني) | 10 أسئلة | Multiple Choice + Matching شامل مع صور CDN | Boss Level |

#### التحويلات التي أُجريت على البيانات الخام (المستوى الثاني):

| التحويل | التفاصيل |
|---------|----------|
| `fill_in_the_blank` → `multiple_choice` | الأسئلة الأصلية استخدمت `options` + `correct_answer_index` (بنية MC فعلياً) |
| إضافة `sources` | مراجع شافعية موثقة بصيغة `{"book": "...", "link": "..."}` |
| إضافة `image_url` | وسوم CDN بصيغة `{{CDN_IMAGE_SALAH_*}}` |

---

### 📂 04 — عقدة الصيام (المستوى الأول) ✅ مكتملة ومحدثة تفاعلياً 100% #جيميني

> **المسار:** `fiqh/04_Sawm/`
> يغطي المستوى الأول أساسيات وشروط وأركان ومبطلات الصوم في المذهب الشافعي.

| الملف | الموضوع | Steps | التنويع التفاعلي | النوع |
|-------|---------|-------|------------------|-------|
| `01_fasting_definition_and_conditions.json` | تعريف الصيام وحكمه وشروط وجوبه وصحته وصوم الصبي | 8 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `02_moon_sighting_and_laylat_al_qadr.json` | ثبوت شهر رمضان ورؤية المنفرد ويوم الشك وليلة القدر | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `03_fasting_intention_and_abstinence.json` | أركان الصوم (النية وتبييتها، وصوم النفل، والإمساك) | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `04_fasting_sunnahs_and_etiquette.json` | سنن الصيام (السحور، تعجيل الفطر، كف اللسان، الجود) | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `05_fasting_invalidators_and_disliked_acts.json` | مبطلات الصوم (المنافذ المفتوحة، القيء، الجماع) ومكروهاته | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `06_boss_level_sawm.json` | 🏆 الامتحان الملكي الشامل — عقدة الصيام (المستوى الأول) | 10 أسئلة | Multiple Choice + Scenario شامل مع صور CDN | Boss Level |

---

### 📂 04 — عقدة الصيام (المستوى الثاني) ✅ مكتملة ومحدثة تفاعلياً 100% #جيميني

> **المسار:** `fiqh/04_Sawm/level_2/`
> يغطي المستوى الثاني المسائل المتقدمة: الأعذار، الكفارة الكبرى، صوم التطوع والمحرم، الاعتكاف، والنذور.

| الملف | الموضوع | Steps | التنويع التفاعلي | النوع |
|-------|---------|-------|------------------|-------|
| `01_fasting_excuses_and_redemption.json` | الأعذار المبيحة للفطر والقضاء والفدية (المرض، السفر، الحامل والمرضع، الهرم) | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `02_fasting_expiation_and_holding_time.json` | الكفارة الكبرى (موجباتها، ترتيب خصالها) والإمساك لحرمة الوقت | 6 | Multiple Choice + Scrambled + Scenario + توثيق | Micro-learning |
| `03_fasting_voluntary_and_prohibited_days.json` | صوم التطوع والأيام المحرمة والمكروهة وصوم النصف الثاني من شعبان | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `04_fasting_i'tikaf_sunnah_and_invalidators.json` | أحكام الاعتكاف، أركانه، مبطلاته، وما يعفى عنه، ومستحباته ومكروهاته | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `05_fasting_vows_and_continuity_rules.json` | أحكام النذر المطلق والمشروط، انقطاع التتابع بالعذر وبغيره، واشتراط الصوم | 6 | Multiple Choice + Fill in Blanks + Scenario + توثيق | Micro-learning |
| `06_boss_level_sawm_l2.json` | 🏆 الامتحان الملكي الشامل — عقدة الصيام (المستوى الثاني) | 10 أسئلة | Multiple Choice شامل وموثق مع صور CDN | Boss Level |
| `fasting_enrichment_misconceptions.json` | 💎 الملحق الإثرائي: مفاهيم خاطئة ومستحبات في الصوم (21 بطاقة نوعية) | 21 بطاقة | 3 فئات (ليست مفطرة، مفطرة/مكروهة، أهم السنن) | إثرائي |

---

## ⚙️ كيفية القراءة في الكود (Dart)

### قراءة درس عادي مع التعامل مع الأنواع التفاعلية الأربعة:
```dart
// lib/services/fiqh_service.dart
import 'dart:convert';
import 'package:flutter/services.dart';

final jsonStr = await rootBundle.loadString('data/fiqh/01_Taharah/01_water_and_purity.json');
final lesson = jsonDecode(jsonStr);
final steps = lesson['steps'] as List;

for (var step in steps) {
  final type = step['type'];
  
  if (type == 'concept') {
    // عرض بطاقة الشرح الموثقة
    final title     = step['title'] as String;
    final content   = step['content'] as String;
    final example   = step['example'] as String?;
    final imageUrl  = step['image_url'] as String?;
    final sources   = (step['sources'] as List?)?.map((s) => {
      'book': s['book'],
      'link': s['link'],
    }).toList();
  } else if (type == 'question') {
    // عرض السؤال التفاعلي بحسب نوعه
    final qType        = step['question_type'] as String;
    final qText        = step['question_text'] as String;
    final explanation  = step['explanation'] as String;
    final imageUrl     = step['image_url'] as String?;

    switch (qType) {
      case 'multiple_choice':
        final options      = List<String>.from(step['options']);
        final correctIndex = step['correct_answer_index'] as int;
        // بناء واجهة الخيارات المتعددة
        break;

      case 'fill_in_the_blanks':
        final correctWords = List<String>.from(step['correct_words']);
        final distractors  = List<String>.from(step['distractors'] ?? []);
        // بناء واجهة سحب الكلمات وإسقاطها في الفراغات
        break;

      case 'scrambled_words':
        final correctOrder = List<String>.from(step['correct_order']);
        // بناء واجهة إعادة الترتيب
        break;

      case 'scenario_based':
        final scenarioText = step['scenario_text'] as String;
        final options      = List<String>.from(step['options']);
        final correctIndex = step['correct_answer_index'] as int;
        // بناء واجهة السيناريو الفقهي مع السؤال الاستنتاجي
        break;
    }
  }
}
```

### قراءة Boss Level:
```dart
final jsonStr = await rootBundle.loadString('data/fiqh/01_Taharah/06_boss_level_taharah.json');
final questions = jsonDecode(jsonStr) as List; // Array مباشر

for (var q in questions) {
  final id          = q['id'];
  final questionText = q['question_text'];
  final imageUrl    = q['image_url'];
  final options     = q['options'] as List;
  final correctIndex = q['correct_answer_index'];
  final explanation  = q['explanation'];
}
```

---

## 📊 إحصائيات المسار (الحالية)

| الإحصاء | القيمة |
|---------|-------|
| العقدات الكاملة والمحدثة | 3 من 5 (الطهارة ✅، الصلاة ✅ مستويين، الصيام ✅ مستويين + إثرائي) |
| إجمالي الملفات الحالية | 31 ملف (6 طهارة + 6 صلاة L1 + 6 صلاة L2 + 6 صيام L1 + 7 صيام L2) |
| إجمالي Steps الحالية | ~201 step + 21 بطاقة إثرائية |
| أنواع الأسئلة المفعلة | 5 أنواع (Multiple Choice, Fill in Blanks, Scrambled, Scenario, Matching) |
| أسئلة Boss الحالية | 45 سؤال (5 طهارة + 10 صلاة L1 + 10 صلاة L2 + 10 صيام L1 + 10 صيام L2) ✅ |
| المذهب المعتمد | الشافعي |

---

## ⚠️ ملاحظات مهمة للمطور

> **1. الهيكل التفاعلي الجديد:**
> تم تطبيق الدليل الصارم `GEMINI_DATA_STRUCTURING_GUIDE.md` بإلزامية إضافة المراجع `sources` لكل بطاقة مفهوم، وإدراج صور الـ CDN، مع التنويع الكامل بين الأسئلة التفاعلية الأربعة بدلاً من الاقتصار على الخيارات المتعددة.

> **2. البيانات الدينية حساسة جداً:**
> كل الأحكام مبنية على المذهب الشافعي. أي تعديل يستوجب مراجعة متخصص فقهي. الخلافات المذهبية مُشار إليها صراحةً في حقل `content` بعلامة [ملاحظة].

> **3. الفرق بين نوعي الملفات:**
> دروس (01→05): `{ "steps": [...] }` ← Object بمفتاح steps
> Boss Level: `[...]` ← Array مباشر بدون Object رئيسي

> **4. الترتيب التعليمي تراكمي:**
> كل عقدة تبني على ما قبلها. الطهارة أساس الصلاة، لا تغيّر الترتيب.

---

## 🔗 ملفات مرجعية أخرى في المشروع

| الملف | الموضوع |
|-------|---------|
| `GEMINI_DATA_STRUCTURING_GUIDE.md` | دليل الذكاء الاصطناعي لإعادة هيكلة البيانات الفقهية (النسخة المحدثة) |
| `heq_werdk_backend/data/fiqh/FIQH_MEDIA_INJECTION_GUIDE.md` | دليل الذكاء الاصطناعي لحقن الوسائط (الصور والصوتيات الحية) |
| `data/tajweed/STRUCTURE_MAP.md` | خريطة مسار التجويد |
| `FIQH_CONTENT_PROMPT.md` | برومتات توليد المحتوى |
| `MASCOT_ANIMATIONS_GUIDE.md` | دليل تميمة التطبيق |
| `DESIGN_3D_GUIDE.md` | دليل الأصول ثلاثية الأبعاد |

---

*آخر تحديث: سبتمبر 2026 — HEQ Werdk Content Team | عقدة الصلاة: #كلاود (Claude)*
