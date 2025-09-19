# بوت تلغرام - وعليكم السلام

بوت تلغرام بسيط مكتوب بـ Python يرد بـ "وعليكم السلام" على أي رسالة يتم إرسالها إليه.

## المميزات

- يرد بـ "وعليكم السلام" على أي رسالة
- واجهة ويب لإدارة البوت وإعداد الـ Webhook
- جاهز للنشر على Render.com
- يدعم الـ Webhooks للاستجابة السريعة

## متطلبات التشغيل

- Python 3.11+
- Flask
- requests
- حساب على Telegram وبوت من @BotFather
- حساب على Render.com للنشر

## إعداد البوت محلياً

1. انسخ المشروع:
```bash
git clone <repository-url>
cd telegram_bot
```

2. إنشاء البيئة الافتراضية وتفعيلها:
```bash
python -m venv venv
source venv/bin/activate  # على Linux/Mac
# أو
venv\\Scripts\\activate  # على Windows
```

3. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

4. إعداد متغيرات البيئة:
```bash
cp .env.example .env
# عدل ملف .env وأضف BOT_TOKEN الخاص بك
```

5. تشغيل التطبيق:
```bash
python src/main.py
```

6. افتح المتصفح على `http://localhost:5000`

## النشر على Render.com

### الطريقة الأولى: استخدام GitHub

1. ارفع المشروع إلى GitHub
2. اذهب إلى [Render.com](https://render.com) وسجل دخولك
3. اضغط على "New" ثم "Web Service"
4. اربط حسابك بـ GitHub واختر المستودع
5. اختر الإعدادات التالية:
   - **Name**: اسم التطبيق (مثل: telegram-bot-salam)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python src/main.py`
6. في قسم "Environment Variables" أضف:
   - `BOT_TOKEN`: التوكن الخاص ببوتك من @BotFather
   - `PYTHON_VERSION`: 3.11.0
7. اضغط "Create Web Service"

### الطريقة الثانية: استخدام render.yaml

1. تأكد من وجود ملف `render.yaml` في جذر المشروع
2. ارفع المشروع إلى GitHub
3. في Render، اختر "New" ثم "Blueprint"
4. اربط المستودع واتبع التعليمات

## إعداد الـ Webhook

بعد نشر التطبيق على Render:

1. انسخ رابط التطبيق من Render (مثل: `https://your-app.onrender.com`)
2. افتح التطبيق في المتصفح
3. في قسم "إعداد الـ Webhook"، أدخل الرابط: `https://your-app.onrender.com/telegram/webhook`
4. اضغط "تعيين الـ Webhook"
5. تأكد من ظهور رسالة نجاح

## اختبار البوت

1. ابحث عن بوتك في تلغرام باستخدام اسم المستخدم الذي حصلت عليه من @BotFather
2. ابدأ محادثة مع البوت
3. أرسل أي رسالة
4. يجب أن يرد البوت بـ "وعليكم السلام"

## استكشاف الأخطاء

### البوت لا يرد على الرسائل

1. تأكد من أن BOT_TOKEN صحيح
2. تحقق من إعداد الـ Webhook في واجهة الويب
3. راجع سجلات Render للأخطاء

### خطأ في النشر

1. تأكد من أن جميع الملفات موجودة (requirements.txt, Procfile)
2. تحقق من أن Python version صحيح
3. راجع سجلات البناء في Render

### مشاكل الـ Webhook

1. تأكد من أن الرابط صحيح وينتهي بـ `/telegram/webhook`
2. تحقق من أن التطبيق يعمل ويمكن الوصول إليه
3. استخدم "معلومات الـ Webhook" للتحقق من الحالة

## هيكل المشروع

```
telegram_bot/
├── src/
│   ├── routes/
│   │   ├── telegram.py      # معالج الـ Webhook والـ API
│   │   └── user.py          # API المستخدمين (من القالب)
│   ├── models/
│   │   └── user.py          # نماذج قاعدة البيانات
│   ├── static/
│   │   └── index.html       # واجهة الويب
│   └── main.py              # نقطة دخول التطبيق
├── requirements.txt         # متطلبات Python
├── Procfile                 # أمر التشغيل لـ Render
├── render.yaml              # إعدادات Render
├── .env.example             # مثال على متغيرات البيئة
└── README.md                # هذا الملف
```

## API Endpoints

- `GET /`: الصفحة الرئيسية
- `POST /telegram/webhook`: استقبال تحديثات تلغرام
- `POST /telegram/set_webhook`: تعيين رابط الـ Webhook
- `GET /telegram/get_webhook_info`: معلومات الـ Webhook الحالي
- `GET /telegram/health`: فحص حالة البوت

## الدعم

إذا واجهت أي مشاكل:

1. تحقق من سجلات Render
2. تأكد من صحة BOT_TOKEN
3. راجع واجهة الويب لحالة البوت
4. تحقق من إعدادات الـ Webhook

## الترخيص

هذا المشروع مفتوح المصدر ومتاح للاستخدام الحر.

