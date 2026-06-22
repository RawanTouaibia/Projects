# Currency Logger

A Python script that automatically logs currency exchange rates to Google Sheets.

## What it does
Fetches USD, EUR, and GBP rates against DZD and logs them with date and time to a Google Sheet.

## How to run
1. pip install gspread google-auth requests
2. Add your credentials.json file
3. Add your Sheet ID in the code
4. Run: python main.py

## Libraries used
- gspread
- google-auth
- requests
- datetime