# ⚽ Match Analysis Betting Bot

بوت ذكي لتحليل مباريات كرة القدم والتنبؤ بالنتائج.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 المميزات

✅ **تحليل إحصائي متقدم** - تحليل شامل للمباريات بناءً على البيانات الحقيقية
✅ **توقعات دقيقة** - تنبؤ بنتائج المباريات مع النسب المئوية
✅ **تحليل الأهداف** - Over/Under مع الاحتمالات
✅ **تحليل الركنيات** - توقع عدد الركنيات المتوقعة
✅ **بيانات الفريقين** - أداء البيت والخارج والإصابات
✅ **واجهة سهلة** - بوت Telegram سهل الاستخدام

## 🚀 البدء السريع

### المتطلبات
- Python 3.8+
- Telegram Account
- football-data.org API Key

### التثبيت

1. **استنساخ المشروع**
```bash
git clone https://github.com/dris-betting-bot/match-analysis-bot.git
cd match-analysis-bot
```

2. **تثبيت المكتبات**
```bash
pip install -r requirements.txt
```

3. **إعداد البيئة**
```bash
cp .env.example .env
# ثم أضف توكن Telegram و API Key إلى ملف .env
```

4. **تشغيل البوت**
```bash
python main.py
```

## 📚 كيفية الاستخدام

أرسل للبوت على Telegram:

```
/start              - البدء والترحيب
/help               - المساعدة
/about              - معلومات عن البوت

ريال مدريد vs برشلونة         - تحليل المباراة
LA Galaxy vs Colorado Rapids   - تحليل أخرى
```

## 📊 المخرجات

البوت يعطيك:

- 🎯 **توقع النتيجة** مع النسب المئوية (فوز/تعادل/خسارة)
- ⚽ **توقع الأهداف** (Over 2.5, Under 2.5, إلخ)
- 🚩 **توقع الركنيات**
- 📈 **إحصائيات الفريقين**
- ⚠️ **ملاحظات مهمة** عن الفريقين

## 🏗️ البنية

```
match-analysis-bot/
├── main.py              # البوت الرئيسي
├── analyzer.py          # محلل المباريات
├── requirements.txt     # المكتبات المطلوبة
├── Procfile            # تكوين Heroku
├── .env.example        # مثال البيئة
└── README.md           # هذا الملف
```

## 🔑 الحصول على المفاتيح

### 1. Telegram Bot Token
- افتح Telegram وابحث عن `@BotFather`
- اتبع التعليمات لإنشاء بوت جديد
- انسخ التوكن الذي تحصل عليه

### 2. Football Data API Key
- اذهب إلى https://www.football-data.org/
- أنشئ حساب مجاني
- احصل على API Key من الإعدادات

## 🌐 النشر على السحابة

### Heroku

```bash
# تثبيت Heroku CLI
# ثم قم بـ:

heroku login
heroku create your-app-name
heroku config:set TELEGRAM_TOKEN=your_token
heroku config:set FOOTBALL_API_KEY=your_api_key
git push heroku main
heroku logs --tail
```

### AWS / Google Cloud
يمكن استخدام Cloud Run أو Lambda لتشغيل البوت بدون تكاليف إضافية.

## 📝 الترخيص

MIT License - انظر LICENSE للتفاصيل

## 🤝 المساهمة

نرحب بالمساهمات! يمكنك:
- الإبلاغ عن الأخطاء
- اقتراح ميزات جديدة
- تحسين الكود

## 📧 التواصل

- Email: support@dris.bot
- GitHub: @dris-betting-bot

## ⚠️ تنبيه مهم

هذا البوت للتحليل فقط. الرهانات تحمل مخاطر، تأكد من معرفتك بما تفعله قبل الرهان.

---

صنع بـ ❤️ بواسطة Dris Betting Bot
