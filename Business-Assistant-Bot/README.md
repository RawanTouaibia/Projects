# Business Assistant Bot

A Telegram bot that receives customer orders and logs them automatically to Google Sheets.

## Features
- /start - Welcome message
- /order - Send your order
- /help  - Show available commands
- Orders are saved automatically to Google Sheets with username, date and time

## How to run
1. pip install python-telegram-bot nest_asyncio gspread google-auth
2. Add your credentials.json file
3. Add your Telegram token and Sheet ID in the code
4. Run on Google Colab

## Libraries used
- python-telegram-bot
- gspread
- google-auth
- datetime