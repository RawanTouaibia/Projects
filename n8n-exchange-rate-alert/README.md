# n8n Exchange Rate Alert Workflow

workflow أتمتة يراقب سعر الدينار الجزائري كل ساعة 
ويرسل تنبيه على تيليغرام عند تجاوز السعر حداً معيناً.

## المكونات
- Schedule Trigger: تشغيل تلقائي كل ساعة
- HTTP Request: جلب أسعار الصرف من Exchange Rate API
- IF Node: شرط منطقي للتحقق من السعر
- Telegram Node: إرسال تنبيه فوري عند تحقق الشرط

## الإعداد
1. استورد ملف workflow.json في n8n
2. أضف Telegram Bot Token في Credentials
3. عدّل YOUR_CHAT_ID برقمك من @userinfobot
4. عدّل الحد السعري في عقدة IF حسب احتياجك

## التقنيات
n8n | Exchange Rate API | Telegram Bot API