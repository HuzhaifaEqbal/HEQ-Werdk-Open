# 🗺️ خريطة ومنهج مسار التجويد - HEQ Werdk
## (Tajweed Curriculum Structure Map & Interactive Node Registry)

> ### 📌 الوظائف والمهام الأساسية لهذا الملف (File Functions & Scope):
> * **خريطة أبواب التجويد العشرة:** من مبادئ التجويد والمخارج والصفات وأحكام النون والميم وحتى الوقف والابتداء.
> * **هيكلة ملفات الـ JSON الـ 50:** توثيق كل درس وتصنيف ملفات الشرح واختبارات الـ Boss Level لكل جزء.
> * **معايير Micro-learning للتجويد:** التناوب بين المفهوم والشاهد القرآني والسؤال التطبيقي.
> * **الفئة المستهدفة:** مهندسو الواجهة الخلفية، مطورو الواجهات، ومصممو المناهج القرآنية.

---

## 📁 المسار الجذري
```
heq_werdk_backend/data/tajweed/
```

---

## 🏗️ البنية العامة للمجلدات

```
tajweed/
├── 01_Basics_and_Makharij/
├── 02_Sifat_Al_Huroof/
├── 03_Nun_Sakinah_and_Tanween/
├── 04_Meem_Sakinah_and_Mushaddadah/
├── 05_Madd_Rules_Part_1/
├── 06_Madd_Rules_Part_2/
├── 07_Tafkheem_and_Tarqeeq/
├── 08_Relations_Between_Letters/
├── 09_Hamzat_and_Waqf/
└── 10_Maqtoo_Mawsool_and_Conclusion/
```

كل مجلد يحتوي على **5 ملفات JSON**:
- `01_*.json` → `04_*.json` : دروس Micro-learning (تم تحويلها)
- `05_boss_level_*.json` : اختبار نهائي شامل (لم يُعدَّل)

---

## 📐 هيكل ملفات الدروس (01 → 04)

> **نمط Micro-learning** — كل ملف = 10 خطوات (5 شرح + 5 سؤال)

```json
{
  "steps": [
    {
      "type": "concept",
      "title": "عنوان المفهوم",
      "content": "شرح المفهوم العلمي بدقة",
      "example": "مثال قرآني أو تطبيقي"
    },
    {
      "type": "question",
      "question_type": "multiple_choice",
      "question_text": "السؤال",
      "options": ["خيار1", "خيار2", "خيار3", "خيار4"],
      "correct_answer_index": 0,
      "explanation": "شرح الإجابة الصحيحة"
    }
  ]
}
```

### قواعد البنية:
| الحقل | النوع | الوصف |
|-------|-------|-------|
| `steps` | `Array` | مصفوفة الخطوات (10 عناصر) |
| `type` | `"concept"` أو `"question"` | نوع الخطوة |
| `title` | `String` | عنوان بطاقة المفهوم (للـ concept فقط) |
| `content` | `String` | نص الشرح العلمي (للـ concept فقط) |
| `example` | `String` | مثال قرآني أو تطبيقي (للـ concept فقط) |
| `question_type` | `"multiple_choice"` | نوع السؤال (للـ question فقط) |
| `question_text` | `String` | نص السؤال (للـ question فقط) |
| `options` | `Array[String]` | 4 خيارات (للـ question فقط) |
| `correct_answer_index` | `Number (0-3)` | رقم الخيار الصحيح (للـ question فقط) |
| `explanation` | `String` | شرح الإجابة الصحيحة (للـ question فقط) |

---

## 📐 هيكل ملفات Boss Level (05)

> **اختبار نهائي** — لم يُعدَّل — يحتوي على 10 أسئلة بهيكل مختلف

```json
[
  {
    "id": "q_unique_id",
    "type": "multiple_choice",
    "question_text": "السؤال",
    "options": ["خيار1", "خيار2", "خيار3", "خيار4"],
    "correct_answer_index": 0,
    "explanation": "شرح الإجابة"
  }
]
```

> ⚠️ **تنبيه للمطور:** ملفات Boss تُقرأ كـ `Array` مباشرة (لا يوجد object رئيسي)، بينما ملفات الدروس تُقرأ كـ `Object` يحتوي على مفتاح `steps`.

---

## 📚 قائمة الملفات الكاملة (50 ملف)

### 📂 01 — أساسيات التجويد ومخارج الحروف
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_intro_and_importance.json` | مقدمة التجويد وأهميته | Micro-learning |
| `02_makharij_jawf_halq.json` | مخارج الجوف والحلق | Micro-learning |
| `03_makharij_lisan.json` | مخارج اللسان | Micro-learning |
| `04_makharij_shafatain_khayshum.json` | مخارج الشفتين والخيشوم | Micro-learning |
| `05_boss_level_makharij.json` | 🏆 اختبار المخارج النهائي | Boss Level |

### 📂 02 — صفات الحروف
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_sifat_intro.json` | مقدمة الصفات | Micro-learning |
| `02_sifat_with_opposites.json` | الصفات ذات الأضداد | Micro-learning |
| `03_sifat_without_opposites_1.json` | الصفات بلا ضد (الجزء الأول) | Micro-learning |
| `04_sifat_without_opposites_2.json` | الصفات بلا ضد (الجزء الثاني) | Micro-learning |
| `05_boss_level_sifat.json` | 🏆 اختبار الصفات النهائي | Boss Level |

### 📂 03 — النون الساكنة والتنوين
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_izhar_halqi.json` | الإظهار الحلقي | Micro-learning |
| `02_idgham.json` | الإدغام (بغنة وبغير غنة) | Micro-learning |
| `03_iqlab.json` | الإقلاب | Micro-learning |
| `04_ikhfa_haqiqi.json` | الإخفاء الحقيقي | Micro-learning |
| `05_boss_level_nun.json` | 🏆 اختبار النون النهائي | Boss Level |

### 📂 04 — الميم الساكنة والمشددة
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_ikhfa_shafawi.json` | الإخفاء الشفوي | Micro-learning |
| `02_idgham_shafawi.json` | الإدغام الشفوي | Micro-learning |
| `03_izhar_shafawi.json` | الإظهار الشفوي | Micro-learning |
| `04_nun_meem_mushaddadah.json` | النون والميم المشددتان | Micro-learning |
| `05_boss_level_meem.json` | 🏆 اختبار الميم النهائي | Boss Level |

### 📂 05 — أحكام المد (الجزء الأول)
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_madd_tabii.json` | المد الطبيعي (الأصلي) | Micro-learning |
| `02_madd_awad.json` | مد العوض | Micro-learning |
| `03_madd_badal.json` | مد البدل | Micro-learning |
| `04_madd_silah_sughra.json` | مد الصلة الصغرى | Micro-learning |
| `05_boss_level_madd_1.json` | 🏆 اختبار المد الجزء الأول | Boss Level |

### 📂 06 — أحكام المد (الجزء الثاني)
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_madd_muttasil.json` | المد المتصل | Micro-learning |
| `02_madd_munfasil_and_kubra.json` | المد المنفصل والصلة الكبرى | Micro-learning |
| `03_madd_aaridh_and_leen.json` | مد العارض للسكون ومد اللين | Micro-learning |
| `04_madd_laazim.json` | المد اللازم | Micro-learning |
| `05_boss_level_madd_2.json` | 🏆 اختبار المد الجزء الثاني | Boss Level |

### 📂 07 — التفخيم والترقيق
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_tafkheem_and_tarqeeq_basics.json` | أساسيات التفخيم والترقيق | Micro-learning |
| `02_laam_lafth_aljalalah.json` | لام لفظ الجلالة | Micro-learning |
| `03_raa_tafkheem.json` | تفخيم الراء وحالاته | Micro-learning |
| `04_raa_tarqeeq_and_jawaaz.json` | ترقيق الراء وحالات الجواز | Micro-learning |
| `05_boss_level_tafkheem.json` | 🏆 اختبار التفخيم والترقيق | Boss Level |

### 📂 08 — العلاقات بين الحروف
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_mutamathilayn.json` | المتماثلان | Micro-learning |
| `02_mutajanisayn.json` | المتجانسان | Micro-learning |
| `03_mutaqaribayn.json` | المتقاربان | Micro-learning |
| `04_types_of_relations.json` | أنواع العلاقات (الصغير/الكبير/المطلق) | Micro-learning |
| `05_boss_level_relations.json` | 🏆 اختبار العلاقات النهائي | Boss Level |

### 📂 09 — الهمزات والوقف
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_hamzat_wasl_verbs.json` | همزة الوصل في الأفعال | Micro-learning |
| `02_hamzat_wasl_nouns.json` | همزة الوصل في الأسماء | Micro-learning |
| `03_waqf_types.json` | أنواع الوقف (تام/كافي/حسن/قبيح) | Micro-learning |
| `04_waqf_signs.json` | علامات الوقف في المصحف | Micro-learning |
| `05_boss_level_waqf.json` | 🏆 اختبار الهمزات والوقف | Boss Level |

### 📂 10 — المقطوع والموصول والخاتمة
| الملف | الموضوع | النوع |
|-------|---------|-------|
| `01_maqtoo_and_mawsool_basics.json` | أساسيات المقطوع والموصول | Micro-learning |
| `02_taat_al_taneeth.json` | تاءات التأنيث (مفتوحة / مربوطة) | Micro-learning |
| `03_special_words_and_exceptions.json` | الكلمات الخاصة والسكتات والإشمام | Micro-learning |
| `04_tajweed_mastery_final.json` | خاتمة التجويد: التعريف والمراتب والأحكام | Micro-learning |
| `05_boss_level_grand_finale.json` | 🏆 الاختبار الملكي الختامي | Boss Level |

---

## ⚙️ كيفية القراءة في الكود

### قراءة ملف درس عادي (01 → 04):
```javascript
const lesson = JSON.parse(fs.readFileSync('01_izhar_halqi.json'));
const steps = lesson.steps; // Array of 10 steps

steps.forEach(step => {
  if (step.type === 'concept') {
    // عرض بطاقة الشرح
    console.log(step.title, step.content, step.example);
  } else if (step.type === 'question') {
    // عرض سؤال الاختبار
    console.log(step.question_text, step.options, step.correct_answer_index);
  }
});
```

### قراءة ملف Boss Level (05):
```javascript
const bossQuestions = JSON.parse(fs.readFileSync('05_boss_level_nun.json'));
// bossQuestions هو Array مباشرة (لا يوجد مفتاح steps)

bossQuestions.forEach(q => {
  console.log(q.id, q.question_text, q.options, q.correct_answer_index);
});
```

---

## 📊 الإحصائيات

| الإحصاء | القيمة |
|---------|-------|
| إجمالي المجلدات | 10 مجلدات |
| إجمالي الملفات | 50 ملف JSON |
| ملفات Micro-learning | 40 ملف |
| ملفات Boss Level | 10 ملفات |
| خطوات لكل درس | 10 خطوات (5 شرح + 5 سؤال) |
| أسئلة في كل Boss | 10 أسئلة |
| إجمالي خطوات الدروس | 400 خطوة |
| إجمالي أسئلة Boss | 100 سؤال |

---

## ⚠️ ملاحظات مهمة للمطور

> **1. الهيكل مختلف بين نوعي الملفات:**
> - الدروس (01-04): `{ "steps": [...] }` ← Object بمفتاح steps
> - Boss (05): `[...]` ← Array مباشر بدون Object رئيسي

> **2. البيانات دينية حساسة:**
> لا تُعدِّل محتوى الملفات يدوياً دون مراجعة متخصص في علم التجويد.

> **3. رواية حفص:**
> جميع الأحكام والأمثلة مبنية على رواية حفص عن عاصم (الرواية الأكثر انتشاراً في العالم العربي).

> **4. الترتيب منطقي تراكمي:**
> المجلدات مرتبة تعليمياً — كل مجلد يبني على ما قبله. لا تغيّر الترتيب.

---

*آخر تحديث: سبتمبر 2026*
