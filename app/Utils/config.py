import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()


def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")

    if not credentials_path:
        raise ValueError("Google Sheets credentials path not found in environment variables.")

    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(creds)

    try:
        sheet = client.open(os.getenv("GOOGLE_SHEETS_NAME"))
        return sheet
    except gspread.SpreadsheetNotFound:
        raise ValueError(f"Google Sheet with name '{sheet}' not found.")
