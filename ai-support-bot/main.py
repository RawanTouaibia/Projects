import cohere
import nest_asyncio
nest_asyncio.apply()

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = "your_telegram_token_here"
API_KEY = "your_cohere_api_key_here"
client = cohere.ClientV2(API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat(
        model="command-r-plus-08-2024",
        messages = [
            {"role": "system", "content": """
You are a helpful customer support assistant.
Your answers are short, friendly and professional.
"""},
            {"role": "user", "content": user_message}
        ]
    )
    await update.message.reply_text(response.message.content[0].text)

requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/deleteWebhook?drop_pending_updates=true")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))
app.run_polling() 

