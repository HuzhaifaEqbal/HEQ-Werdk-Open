# 🧠 خوارزميات مقترحة لأنظمة الاختبارات والمراجعة القرآنية
## (Recommended Quranic Quiz & Retention Algorithms for Developers)

> ⚠️ **تنويه هام للمطورين (Important Developer Notice):**  
> الخوارزميات والمعادلات ونماذج الشيفرات الموضحة في هذا المستند هي **اقتراحات ونماذج استرشادية قياسية** نقترحها على المطورين للاستفادة منها عند بناء محركات الاختبارات الذكية وجدولة المراجعة التفاعلية في تطبيقاتهم القرآنية.  
> **هذه النماذج لا تمثل ولا تطابق الخوارزميات الداخلية أو الملكية الخاصة بتطبيق HEQ Werdk**، بل هي حلول برمجية مقترحة ومفتوحة للاسترشاد والتطوير الحر للاستفادة القصوى من بيانات وعقد واحة القرآن (`quran_oasis`).

---

## 🎯 مقدمة
تحتوي واحة القرآن الكريم (`quran_oasis`) على **1,135 عقدة تفاعلية** و **13,188 نشاطاً تعليمياً** تغطي المصحف الشريف كاملاً (114 سورة موزعة على 30 جزءاً). للاستفادة من هذه البيانات في بناء تجربة تطبيق ذكية للامتحانات وتثبيت الحفظ، نقترح على المطورين تطبيق إحدى أو كلا الخوارزميتين التاليتين:

1. **الخوارزمية الأولى:** خوارزمية التكرار المتباعد التكيفي (Adaptive Spaced Repetition) لجدولة المراجعة وتثبيت المحفوظ.
2. **الخوارزمية الثانية:** خوارزمية التوليد التكيفي للاختبارات والمشتتات الذكية (Adaptive Quiz & Distractor Generator) لإنشاء اختبارات عادلة وديناميكية مع الالتزام التام بالضابط الشرعي (**حظر بعثرة كلمات القرآن الكريم مطلقاً**).

---

## 1. الخوارزمية المقترحة الأولى: التكرار المتباعد التكيفي (Quranic Spaced Repetition)

### 📌 الفكرة النظرية
تعتمد هذه الخوارزمية على تكييف خوارزمية **SuperMemo (SM-2)** الشهيرة لتلائم خصوصية الحفظ القرآني؛ حيث ترتكز على منحنى النسيان (Forgetting Curve) لحساب الموعد الأمثل لمراجعة كل عقدة قرآنية (`nodeId`)، مع ضبط حد أقصى للفاصل الزمني لا يتجاوز 30 يوماً (لضمان تعاهد القرآن والختم الشهري وفق الهدي النبوي).

### 📐 المعادلات الحسابية المقترحة
عند انتهاء المستخدم من مراجعة أو اختبار عقدة قرآنية، يُسجّل تقييم أدائه بدرجة \(q\) من 0 إلى 5 (حيث 5 = إتقان تام دون تردد، 0 = تعثر كامل):

1. **تحديث معامل السهولة (Ease Factor - \(EF\)):**
   \[
   EF' = \max\left(1.3, \; EF + \left(0.1 - (5 - q) \times (0.08 + (5 - q) \times 0.02)\right)\right)
   \]
2. **حساب الفاصل الزمني القادم بالأيام (\(I\)):**
   - إذا كان \(q < 3\) (لم يُتقن الحفظ): يعاد التكرار فوراً:
     \[
     \text{Repetitions} = 0, \quad I = 1
     \]
   - إذا كان \(q \ge 3\) (أتقن الحفظ):
     - للمرة الأولى (\(n = 1\)): \(I_1 = 1 \text{ يوم}\)
     - للمرة الثانية (\(n = 2\)): \(I_2 = 3 \text{ أيام}\)
     - للمرات اللاحقة (\(n > 2\)): 
       \[
       I_n = \min\left(30, \; \text{round}(I_{n-1} \times EF')\right)
       \]

### 💻 نموذج تنفيذي بلغة Dart (Flutter)
```dart
class QuranReviewItem {
  final String nodeId;
  int repetitions;
  double easeFactor;
  int intervalDays;
  DateTime nextReviewDate;

  QuranReviewItem({
    required this.nodeId,
    this.repetitions = 0,
    this.easeFactor = 2.5,
    this.intervalDays = 0,
    required this.nextReviewDate,
  });

  /// خوارزمية مقترحة لتحديث جدولة مراجعة العقدة القرآنية
  void calculateNextReview(int qualityGrade) {
    // qualityGrade: من 0 إلى 5
    assert(qualityGrade >= 0 && qualityGrade <= 5);

    if (qualityGrade < 3) {
      // إعادة الجدولة لليوم التالي عند التعثر
      repetitions = 0;
      intervalDays = 1;
    } else {
      if (repetitions == 0) {
        intervalDays = 1;
      } else if (repetitions == 1) {
        intervalDays = 3;
      } else {
        intervalDays = (intervalDays * easeFactor).round();
        // سقف الحفظ القرآني: لا تترك آية دون تعاهد أكثر من 30 يوماً
        if (intervalDays > 30) intervalDays = 30;
      }
      repetitions += 1;
    }

    // حساب معامل الصعوبة الجديد
    easeFactor = easeFactor + (0.1 - (5 - qualityGrade) * (0.08 + (5 - qualityGrade) * 0.02));
    if (easeFactor < 1.3) easeFactor = 1.3;

    nextReviewDate = DateTime.now().add(Duration(days: intervalDays));
  }
}
```

---

## 2. الخوارزمية المقترحة الثانية: التوليد التكيفي للاختبارات والمشتتات (Adaptive Quiz Generator)

### 📌 الفكرة النظرية
عند اختبار المستخدم في حفظ عقدة أو سورة، يجب توليد خيارات مضللة (Distractors) ذكية وعالية الدقة للأسئلة مع الالتزام بالضوابط الشرعية التالية:
1. **الالتزام بقدسية القرآن:** يُمنع منعاً باتاً خلط أو بعثرة الآيات (No Scrambled Sentences).
2. **الخيارات المضللة الذكية (Smart Distractors):** بدلاً من وضع كلمات عشوائية لا تمت للسياق بصلة، تقترح الخوارزمية انتقاء الخيارات المضللة من:
   - كلمات مماثلة وزناً أو رسماً من نفس السورة أو الربع.
   - الآيات المتشابهة في نهايات الفواصل (مثل: "عَلِيمٌ حَكِيمٌ" مقابل "حَكِيمٌ عَلِيمٌ" أو "غَفُورٌ رَحِيمٌ").
   - فواتح الآيات المجاورة في نفس السورة عند أسئلة (تخمين الآية التالية).

### 📐 خطوات عمل الخوارزمية المقترحة
1. **تحليل مستوى إتقان المستخدم (Skill Level):**
   - **مبتدئ (Beginner):** تكون الفراغات مقتصرة على فواصل الآيات والكلمات المميزة، مع 3 خيارات فقط.
   - **متوسط (Intermediate):** فراغات في أواسط الآيات وخيارات من السورة نفسها.
   - **متقدم (Advanced):** فراغات في المتشابهات اللفظية الدقيقة مع خيارات متقاربة جداً في الإعراب والرسم.
2. **توليد السؤال ديناميكياً من ملف JSON الخاص بالعقدة:**
   - قراءة مصفوفة `activities` داخل العقدة (`node_xxx.json`).
   - استخراج السؤال المستهدف وفصل الجواب الصحيح.
   - استدعاء مجموعة الكلمات البديلة من مصفوفة `options` المرفقة في العقدة أو من العقد المجاورة.

### 💻 نموذج تنفيذي بلغة TypeScript / JavaScript
```typescript
interface QuizActivity {
  id: string;
  type: 'fill_blank' | 'next_ayah';
  prompt: string;
  correctAnswer: string;
  options: string[];
}

interface GeneratedQuestion {
  questionId: string;
  type: string;
  prompt: string;
  shuffledOptions: string[];
  correctAnswerIndex: number;
}

/**
 * دالة مقترحة لتوليد وتجهيز أنشطة الاختبار من عقدة واحة القرآن
 */
export function buildAdaptiveQuiz(
  activities: QuizActivity[],
  maxQuestions: number = 5
): GeneratedQuestion[] {
  // 1. فرز الأنشطة وانتقاء عينة عشوائية متوازنة
  const selected = [...activities]
    .sort(() => Math.random() - 0.5)
    .slice(0, maxQuestions);

  // 2. صياغة كل سؤال وخلط خيارات الإجابة فقط (دون مساس بنص الآية)
  return selected.map((act, index) => {
    // خلط مصفوفة الخيارات بصورة محايدة
    const uniqueOptions = Array.from(new Set([act.correctAnswer, ...act.options]));
    const shuffled = uniqueOptions.sort(() => Math.random() - 0.5);

    return {
      questionId: `q_${index + 1}_${act.id}`,
      type: act.type,
      prompt: act.prompt,
      shuffledOptions: shuffled,
      correctAnswerIndex: shuffled.indexOf(act.correctAnswer),
    };
  });
}
```

---

## 💡 نصائح إضافية للمطورين (Best Practices)
1. **التخزين المؤقت المحلي (Offline First):** يُنصح بتحميل بيانات العقد القرآنية وتخزينها محلياً (باستخدام SQLite أو Hive في Flutter) عند أول طلب، لضمان عمل المراجعة والاختبارات بدون إنترنت.
2. **ربط التفسير عند الخطأ:** عندما يخطئ المستخدم في اختبار آية معينة، اقترح عليه عرض تفسير الآية من الـ API المعتمد لتثبيت المعنى في الذهن قبل إعادة المحاولة.
3. **التشجيع بدون إخلال:** استخدام نظام النقاط والتسلسل اليومي (Daily Streaks) لتحفيز المستخدم على تعاهد ورده اليومي بانتظام.
