# n8n Exchange Rate Logger

Automated workflow that fetches USD/DZD exchange rate daily and logs it to Google Sheets automatically.

## Workflow
Schedule Trigger → HTTP Request → Google Sheets

## Tech Stack
- n8n
- Exchange Rate API
- Google Sheets API

## Output
| Date | Currency | Rate |
|------|----------|------|
| 2026-07-04 | DZD | 133.33 |

## Setup
1. Import `workflow.json` into n8n
2. Add Google Sheets OAuth2 credentials
3. Replace `YOUR_GOOGLE_SHEET_URL` with your spreadsheet URL
4. Publish the workflow