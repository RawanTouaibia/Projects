import gspread
from google.oauth2.service_account import Credentials
import requests
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

SHEET_ID = "1hMdXSJnG77v1bwQ8gnLTzECWDWzkQFwfQ4SnBnKwLGU"
sheet = client.open_by_key(SHEET_ID).sheet1

def get_rates():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/DZD")
    data = response.json()
    usd = round(1 / data["rates"]["USD"], 4)
    eur = round(1 / data["rates"]["EUR"], 4)
    gbp = round(1 / data["rates"]["GBP"], 4)
    return usd, eur, gbp

def log_to_sheet():
    usd, eur, gbp = get_rates()
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    sheet.append_row([date, time, usd, eur, gbp])
    print(f"Logged: {date} {time} | USD={usd} EUR={eur} GBP={gbp}")

log_to_sheet()