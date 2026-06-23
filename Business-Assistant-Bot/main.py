import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import gspread
from google.oauth2.service_account import Credentials
import requests
from datetime import datetime

TELEGRAM_TOKEN = "your_telegram_token_here"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

SHEET_ID = "18nVqTmwa8blJehcDcD6JY6wirmeQGh0zT9F2C5kO7HA"
sheet = client.open_by_key(SHEET_ID).sheet1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!")

async def order(update, context):
    if not context.args:
        await update.message.reply_text("Please write your order after /order")
        return
    
    text = " ".join(context.args)
    username = update.effective_user.username
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    
    sheet.append_row([username, text, date, time])
    
    await update.message.reply_text(f"Your order has been received: {text}")
    print(f"Logged: {username} | {text} | {date} {time}")

async def help(update, context):
    await update.message.reply_text("""
Available commands:
/start - Welcome message
/order - Send your order
/help  - Show this message
    """)

requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/deleteWebhook?drop_pending_updates=true")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("order", order))
app.add_handler(CommandHandler("help", help))
app.run_polling()
