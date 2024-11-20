"""Summary
In this snippet, we are defining a set of utility functions that are used by the different parts of the application.
These functions include setting up the Google Sheets API, setting up the Selenium web driver,
and fetching the configuration for the web scraper.
"""

import os

import googleapiclient.discovery
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def get_scraper_config(website_name):
    base_url_key = f"{website_name.upper()}_BASE_URL"
    user_agent_key = "USER_AGENT"

    return {
        "base_url": os.getenv(base_url_key),
        "user_agent": os.getenv(user_agent_key),
    }


def setup_driver(website_name):
    config = get_scraper_config(website_name)
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


def wait_for_page_load(driver, locator_type, locator_value):
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        print("Element found successfully.")
        return
    except TimeoutException:
        print("TimeoutException: Element not found within the given time.")
    except NoSuchElementException:
        print("NoSuchElementException: The element could not be located.")
    except WebDriverException as e:
        print(f"WebDriverException: General WebDriver error occurred. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def youtube_build():
    return googleapiclient.discovery.build(os.getenv("YOUTUBE_API_SERVICE_NAME"),
                                           os.getenv("YOUTUBE_API_VERSION"),
                                           developerKey=os.getenv("YOUTUBE_API_KEY"))
