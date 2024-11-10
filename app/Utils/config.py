import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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


def get_scraper_config():
    return {
        "base_url": os.getenv("ALIBABA_BASE_URL"),
        "user_agent": os.getenv("USER_AGENT"),
        "chromedriver_path": os.getenv("CHROMEDRIVER_PATH"),
    }


def setup_driver():
    config = get_scraper_config()
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument(f"user-agent={config['user_agent']}")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--lang=en-GB.UTF-8")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
