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
        raise ValueError(f"Google Sheet with name '{os.getenv('GOOGLE_SHEETS_NAME')}' not found.")


def get_aliexpress_api_config():
    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("RAPIDAPI_HOST")
    base_url = os.getenv("RAPIDAPI_BASE_URL")

    if not api_key or not api_host or not base_url:
        raise ValueError("Missing AliExpress API configuration in environment variables")

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": api_host
    }

    return base_url, headers
