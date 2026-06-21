import nest_asyncio
nest_asyncio.apply()

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = "your_telegram_token_here"
WEATHER_API_KEY = "your_weather_api_key_here"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Send me a city name and I will tell you the weather!")

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text

    if not city.strip():
        await update.message.reply_text("Please enter a city name")
        return

    try:
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        data = response.json()

        if data["cod"] == "404":
            await update.message.reply_text("City not found")
        else:
            reply = f"""
City: {city}
Temperature: {data['main']['temp']}°C
Weather: {data['weather'][0]['description']}
Humidity: {data['main']['humidity']}%
Wind Speed: {data['wind']['speed']} m/s
            """
            await update.message.reply_text(reply)

    except requests.exceptions.ConnectionError:
        await update.message.reply_text("No internet connection")

requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/deleteWebhook?drop_pending_updates=true")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, weather))
app.run_polling() 
