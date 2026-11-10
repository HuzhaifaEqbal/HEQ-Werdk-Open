# 📜 مواصفات وسجل إنجاز مسار الفقه والعبادات اليومية
## (Fiqh Curriculum Engineering Specification & Media Status Registry)

> ### 📌 الوظائف والمهام الأساسية لهذا الملف (File Functions & Scope):
> * **سجل إنجاز المنهج الفقهي (المذهب الشافعي):** توثيق الدروس المكتملة 100% لعقد الطهارة، الصلاة (المستويين 1 و 2)، والصيام.
> * **القواعد التشغيلية الصارمة:** حظر استخدام التيرمينال لحماية المحارف العربية، منع تكرار الصوتيات، وقواعد الوصف التشريحي للصور.
> * **سجل الصوتيات والروابط المعتمدة:** حصر كافة الشواهد الصوتية (تلاوات آية بآية من سيرفر HEQ CDN) وحصن المسلم لمنع التكرار.
> * **الفئة المستهدفة:** مهندسو مناهج الفقه، مطورو المحتوى الإسلامي، ونماذج الذكاء الاصطناعي المسؤولة عن بناء مسارات الفقه.

---

## 🛑 القواعد التشغيلية الصارمة (Strict Rules) — ممنوع مخالفتها إطلاقاً

### 1. قاعدة منع التيرمينال المطلقة (Zero-Terminal Rule)
* ⚠️ **ممنوع منعاً باتاً استخدام أي أمر تيرمينال / كونسول (مثل `run_command` أو PowerShell).**
* **السبب:** موجه أوامر ويندوز (PowerShell / CMD) يعاني من خلل حاد في معالجة محارف الـ UTF-8 العربية، وتشغيل أي أمر كفيل بإتلاف النصوص العربية، والتشكيل الفقهي، وتحويل الملفات إلى علامات استفهام `???`.
* **طريقة العمل الحصرية:** استخدم دائماً أدوات التحرير المباشرة: `view_file`، `replace_file_content`، و `write_to_file`.

### 2. العمل خطوة بخطوة وملفاً بملف (One File at a Time)
* لا تقم أبداً بمعالجة عدة ملفات دفعة واحدة.
* افتح الملف، راجعه فقهياً، اقترح الصوتيات المناسبة وافحصها، صف الصور وصفاً تشريحياً بالعربية، انتظر روابط الـ CDN من المستخدم، احقنها، تأكد من صحة الـ JSON، ثم انتقل للملف التالي.

### 3. المنع البات لتكرار أي رابط صوتي (No Audio Repetition)
* تم اعتماد قاعدة صارمة: **عدم تكرار أي مقطع صوتي (آية أو ذكر) استُخدم في درس سابق على الإطلاق**.
* استعن بجدول الصوتيات أدناه لمعرفة ما تم استهلاكه.

### 4. قاعدة وصف الصور (Arabic Physical Descriptions Only)
* ⚠️ **ممنوع توليد برومتات إنجليزية لتوليد الصور.**
* **السبب:** محركات التوليد تضع نصوصاً إنجليزية وكلمات لاتينية عشوائية مشوهة داخل الصور.
* **المطلوب بدلاً من ذلك:** تقديم **وصف شكلي تشريحي دقيق باللغة العربية** للمستخدم ليقوم هو بتوليدها، مع التركيز على **الصور المقارنة (Side-by-Side)** لتمييز الصحيح من الباطل أو المكروه.

### 5. عدم حذف وسوم الصور إطلاقاً (Preserve Placeholders)
* إذا قرر المستخدم تخطي إضافة الصور لدرس معين أو لملفات الـ Boss Level، **لا تحذف وسم `{{CDN_IMAGE_...}}` أبداً**؛ اتركه مكانه في ملف الـ JSON ليبقى محفوظاً للاستخدام المستقبلي.

### 6. مصادر الصوتيات المعتمدة
* **الشواهد القرآنية:** من سيرفر HEQ CDN آية بآية حصراً، ويجوز اختيار أي قارئ متوفر فيه (الافتراضي: محمود خليل الحصري مرتل). القاعدة: `https://heq-cdn.b-cdn.net/quran/{reciter}/{type}/{SURAH_3DIGITS}/{AYAH_3DIGITS}.mp3`
* **الأذكار والأدعية:** من تسجيلات حصن المسلم الرسمية (`hisnmuslim.com`).
* لا تستخدم أي سيرفر صوتيات آخر.

---

## 📊 حالة المشروع الحالية (ما تم إنجازه بنسبة 100%)

### 1. عقدة الطهارة (`01_Taharah/`) — مكتملة 100% ✅
* جميع ملفات الدروس (01 إلى 05) + ملف الـ Boss Level (06).
* محقونة بالكامل بالصور المفرغة، الصوتيات الحية، ومصادر الشافعية.

### 2. عقدة الصلاة (`02_Salah/`) — مكتملة 100% بمستوييها ✅
* **المستوى الأول (`level_1/`):** 6 ملفات كاملة محقونة بالوسائط والمصادر.
* **المستوى الثاني (`level_2/`):** 6 ملفات كاملة:
  * `01_congregational_prayer_and_imamate.json` (4 صور + صوتين)
  * `02_traveler_prayer.json` (4 صور + صوتين)
  * `03_friday_prayer.json` (4 صور + صوتين)
  * `04_special_prayers_and_funerals.json` (4 صور + صوتين)
  * `05_prostrations_sahw_tilawah_shukr.json` (3 صور + صوتين)
### 3. عقدة الصيام (`04_Sawm/`)
* **المستوى الأول (`level_1/`):** مكتمل 100% ✅
  * `01_fasting_definition_and_conditions.json` (4 صور CDN + صوتين: الحصري 2:183 وحصن المسلم 176)
  * `02_moon_sighting_and_laylat_al_qadr.json` (3 صور CDN + صوتين: حصن المسلم 175 والحصري 97:1)
  * `03_fasting_intention_and_abstinence.json` (3 صور CDN + صوتين: الحصري 98:5 وحصن المسلم 186)
  * `04_fasting_sunnahs_and_etiquette.json` (3 صور CDN + صوتين: الحصري 2:187 وحصن المسلم 184)
  * `05_fasting_invalidators_and_disliked_acts.json` (3 صور CDN + صوتين: الحصري 2:184 وحصن المسلم 250)
* **المستوى الثاني (`level_2/`):** مكتمل 100% ✅
  * `01_fasting_excuses_and_redemption.json` (3 صور CDN + صوتين: الحصري 4:28 وحصن المسلم 183)
  * `02_fasting_expiation_and_holding_time.json` (3 صور CDN + صوتين: الحصري 58:4 وحصن المسلم 196)
  * `03_fasting_voluntary_and_prohibited_days.json` (3 صور CDN + صوتين: الحصري 33:35 وحصن المسلم 237)
  * `04_fasting_i'tikaf_sunnah_and_invalidators.json` (3 صور CDN + صوتين: الحصري 2:125 وحصن المسلم باب 014)
  * `05_fasting_vows_and_continuity_rules.json` (3 صور CDN + صوتين: الحصري 76:7 وحصن المسلم 136)
  * `06_boss_level_sawm_l2.json` (10 أسئلة موثقة فقهياً مع حفظ وسوم الصور كاملة)

---

## 🎧 السجل الشامل لجميع الصوتيات المستخدمة (ممنوع إعادة استخدامها)

كل رابط أدناه تم فحصه واستهلاكه في الدروس السابقة؛ **لا يجوز تكراره**:

### أ. الشواهد القرآنية (المقرئ الحالي: محمود خليل الحصري — مرتل)
القاعدة: `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/{SURAH_3DIGITS}/{AYAH_3DIGITS}.mp3`

| السورة والآية | الرابط المباشر | الموضوع الفقهي |
|---|---|---|
| الفرقان 48 (25:48) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/025/048.mp3` | طهورية ماء السماء والبحار |
| المدثر 4 (74:4) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/074/004.mp3` | وجوب تطهير الثياب للصلاة |
| المائدة 6 (5:6) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/005/006.mp3` | آية الوضوء الكبرى وأركانه |
| النساء 43 (4:43) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/004/043.mp3` | التيمم وموجبات الغسل |
| البقرة 185 (2:185) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/185.mp3` | فقه الرخص والمشقة تجلب التيسير |
| الإسراء 78 (17:78) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/017/078.mp3` | أوقات الصلوات المفروضة |
| الأعراف 31 (7:31) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/007/031.mp3` | شرط ستر العورة وأخذ الزينة |
| البقرة 144 (2:144) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/144.mp3` | شرط استقبال القبلة الكعبة المشرفة |
| البقرة 238 (2:238) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/238.mp3` | المحافظة على الصلوات والقيام لله |
| آل عمران 43 (3:43) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/003/043.mp3` | القنوت والركوع مع الراكعين |
| المؤمنون 2 (23:2) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/023/002.mp3` | الخشوع ونفي مبطلات الصلاة |
| البقرة 43 (2:43) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/043.mp3` | صلاة الجماعة والركوع مع الراكعين |
| النساء 101 (4:101) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/004/101.mp3` | رخصة قصر الصلاة في السفر |
| الجمعة 9 (62:9) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/062/009.mp3` | السعي لصلاة الجمعة وترك البيع |
| الكوثر 2 (108:2) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/108/002.mp3` | صلاة العيدين والنحر |
| الانشقاق 21 (84:21) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/084/021.mp3` | سجود التلاوة ومشروعيته |
| البقرة 183 (2:183) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/183.mp3` | فرض الصيام ومشروعيته |
| القدر 1 (97:1) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/097/001.mp3` | ليلة القدر وفضل إنزال القرآن |
| البينة 5 (98:5) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/098/005.mp3` | وجوب النية والإخلاص في العبادة |
| البقرة 187 (2:187) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/187.mp3` | وقت السحور والإمساك حتى الليل |
| البقرة 184 (2:184) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/184.mp3` | رخص الصيام ومبطلات الإطعام والقضاء |
| النساء 28 (4:28) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/004/028.mp3` | التخفيف ورخص الأعذار في الصيام |
| المجادلة 4 (58:4) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/058/004.mp3` | ترتيب خصال الكفارة الكبرى |
| الأحزاب 35 (33:35) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/033/035.mp3` | فضل الصيام والتطوع وجزاء الصائمين والصائمات |
| البقرة 125 (2:125) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/002/125.mp3` | الاعتكاف ولزوم المساجد وتطهيرها للعاكفين |
| الإنسان 7 (76:7) | `https://heq-cdn.b-cdn.net/quran/al_husary/murattal/076/007.mp3` | الوفاء بالنذر (يوفون بالنذر ويخافون يوماً) |

### ب. أذكار وأدعية حصن المسلم (الأبواب المباشرة)
القاعدة: `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_{DOOR_3DIGITS}.mp3` أو ملف الصوت المباشر من الفهرس `.../ar/{ID}.mp3`

| رقم الباب / المعرف | الرابط المباشر | الذكر الفقهي |
|---|---|---|
| `006` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_006.mp3` | الذكر بعد الفراغ من الوضوء |
| `014` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_014.mp3` | دعاء دخول المسجد (الاعتكاف ولزوم المساجد) |
| `016` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_016.mp3` | إجابة المؤذن وأذكار الأذان |
| `018` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_018.mp3` | دعاء الركوع (سبحان ربي العظيم) |
| `019` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_019.mp3` | دعاء الرفع من الركوع والاعتدال |
| `020` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_020.mp3` | دعاء السجود (سبحان ربي الأعلى) |
| `022` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_022.mp3` | دعاء سجود التلاوة والشكر |
| `023` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_023.mp3` | ألفاظ التشهد المأثورة |
| `024` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_024.mp3` | الصلاة الإبراهيمية في التشهد الأخير |
| `044` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_044.mp3` | الدعاء للميت في صلاة الجنازة |
| `096` | `https://www.hisnmuslim.com/audio/ar/ar_7esn_AlMoslem_by_Doors_096.mp3` | دعاء السفر وركوب الدابة |
| `136` | `https://www.hisnmuslim.com/audio/ar/136.mp3` | دعاء قضاء الدين والوفاء بالذمة (دين الله أحق أن يقضى) |
| `175` | `https://www.hisnmuslim.com/audio/ar/175.mp3` | دعاء رؤية الهلال (اللهم أهله علينا) |
| `176` | `https://www.hisnmuslim.com/audio/ar/176.mp3` | الدعاء عند إفطار الصائم (ذهب الظمأ) |
| `183` | `https://www.hisnmuslim.com/audio/ar/183.mp3` | الدعاء لمن أطعم الصائم أو المسكين (فدية الإطعام) |
| `184` | `https://www.hisnmuslim.com/audio/ar/184.mp3` | الدعاء لمن فطر صائماً (أفطر عندكم الصائمون) |
| `186` | `https://www.hisnmuslim.com/audio/ar/186.mp3` | ما يقول الصائم إذا سابه أحد (إني صائم) |
| `196` | `https://www.hisnmuslim.com/audio/ar/196.mp3` | دعاء كفارة المجلس والاستغفار والتوبة |
| `237` | `https://www.hisnmuslim.com/audio/ar/237.mp3` | خير الدعاء دعاء يوم عرفة (لا إله إلا الله وحده لا شريك له) |
| `250` | `https://www.hisnmuslim.com/audio/ar/250.mp3` | أذكار الاستغفار والتوبة (صيانة الصيام من اللغو والمكروهات) |

### ج. واجهة الأذكار البرمجية للنصوص والصوت (Hisn Muslim JSON API)
* **الفهرس العام لجميع الأبواب ومعرفاتها:** `https://www.hisnmuslim.com/api/ar/husn_ar.json`
* **صيغة استدعاء نص وصوت الذكر:** `https://www.hisnmuslim.com/api/ar/{SECTION_ID}.json`
  - تعيد هذه الواجهة كائن JSON يحتوي على: النص المشكول بالكامل (`ARABIC_TEXT`)، ورابط ملف الصوت الصافي (`AUDIO`)، وعدد مرات التكرار (`REPEAT`).
  - **مثال دعاء إفطار الصائم (ذهب الظمأ):** `https://www.hisnmuslim.com/api/ar/68.json`
  - **مثال ما يقول الصائم إذا سابه أحد (إني صائم):** `https://www.hisnmuslim.com/api/ar/75.json`
* **طريقة الاستخدام في تطبيق Flutter:** يفحص التطبيق رابط `audio_url`، فإن انتهى بـ `.mp3` قام بتشغيله كصوت مباشر، وإن انتهى بـ `.json` قام بجلب نص الدعاء المشكول وعرضه أو تحويله لصوت (TTS) أو تشغيل الرابط الصوتي المضمن بداخله!

---

## 🖼️ سير عمل الصور وشبكة CDN (Bunny CDN)
* **المسار الأساسي لرفع الصور:** `https://werdk-cdn.b-cdn.net/assets/{مجلد_الموضوع}/{اسم_الملف}.png`
* **المجلدات المستخدمة سابقاً:**
  * الطهارة: `assets/taharah/`
  * الصلاة المستوى 1: `assets/salah4/` وغيرها.
  * صلاة الجماعة: `assets/salah5/`
  * صلاة المسافر: `assets/mosafer/`
  * صلاة الجمعة: `assets/jumah/`
  * الجنائز وسجود السهو: `assets/janazaa/`
* **طريقة فحص الروابط برمجياً:**
  * استخدم أداة `read_url_content` لفحص كل رابط.
  * *ملاحظة تقنية:* عند فحص ملفات الصور `.png` المباشرة، قد تظهر الأداة رسالة مثل: `failed to parse HTML: html: open stack of elements exceeds 512 nodes`؛ هذا يعني نجاح الجلب وحصول استجابة HTTP 200 سليمة لأن الملف صورة ثنائية وليس كود HTML.

---

## 📚 المراجع الفقهية المعتمدة (المذهب الشافعي)
يجب توثيق كل بطاقة `concept` بمراجع شافعية رسمية من المكتبة الشاملة:
1. **متن أبي شجاع (غاية الاختصار):** `https://shamela.ws/book/9780/1`
2. **فتح القريب المجيب لابن قاسم الغزي:** `https://shamela.ws/book/9780`
3. **كفاية الأخيار للحصني:** `https://shamela.ws/book/21571/1`
4. **منهاج الطالبين وعمدة المفتين للنووي:** `https://shamela.ws/book/11818`

---

## 🚀 خطة العمل القادمة: العقدة الثالثة (عقدة الزكاة `03_Zakah`)

* **الموقع:** `heq_werdk_backend/data/fiqh/03_Zakah/`
* **الوضع الحالي:** العقدة قيد التجهيز من قبل المستخدم؛ وسيتم استكمال بياناتها الخام لاحقاً.
* **المطلوب من الوكيل القادم فور استلام البيانات:**
  1. العمل ملفاً بملف (Micro-learning) بمصفوفة `steps` بتناوب صارم (`concept` ⬅️ `question`).
  2. تدقيق المسائل وفق معتمد المذهب الشافعي وتوثيقها بالمصادر الأربعة أعلاه.
  3. اختيار آيات الزكاة المقابلة من سور التوبة والبقرة بدون تكرار الصوتيات السابقة.
  4. كتابة وصف شكلي تشريحي عربي دقيق للصور المقارنة (بدون برومتات إنجليزية).
  5. فحص وحقن الروابط بعد رفعها من المستخدم، مع حفظ وسوم `{{CDN_IMAGE_...}}` في كل خطوة.
