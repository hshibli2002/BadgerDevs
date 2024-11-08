import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class GoogleSheetsHandler:
    def __init__(self, sheet_name):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

        credentials_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")

        if not credentials_path:
            raise ValueError("Google Sheets credentials path not found in environment variables.")

        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
        self.client = gspread.authorize(creds)

        try:
            self.sheet = self.client.open(sheet_name)
        except gspread.SpreadsheetNotFound:
            raise ValueError(f"Google Sheet with name '{sheet_name}' not found.")

    def get_worksheet_data(self, worksheet_name):
        """
        Retrieves all data from a specific worksheet.
        Args:
            worksheet_name (str): The name of the worksheet (tab) in the Google Sheet.
        Returns:
            list of dict: List of rows where each row is a dictionary with column names as keys.
        """
        try:
            worksheet = self.sheet.worksheet(worksheet_name)
            data = worksheet.get_all_records()  # Gets all rows as a list of dictionaries
            return data
        except gspread.WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found in Google Sheet '{self.sheet.title}'.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching data: {str(e)}")