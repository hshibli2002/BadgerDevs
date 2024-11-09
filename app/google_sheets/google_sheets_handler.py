import gspread


class GoogleSheetsHandler:
    def __init__(self, sheet):
        self.sheet = sheet
        print(f"Type of self.sheet: {type(self.sheet)}")

    def get_worksheet_data(self, worksheet_name):
        try:
            worksheet = self.sheet.worksheet(worksheet_name)
            data = worksheet.get_all_records()
            return data
        except gspread.WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found in Google Sheet '{self.sheet.title}'.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching data: {str(e)}")

    def add_user_input(self, keyword):
        try:
            worksheet = self.sheet.worksheet("Sheet1")

            existing_keywords = worksheet.col_values(1)

            if keyword in existing_keywords:
                return {"status": "exists", "message": f"Keyword '{keyword}' already exists in the sheet."}

            worksheet.append_row([keyword])
            return {"status": "added", "message": f"Keyword '{keyword}' added successfully."}

        except gspread.WorksheetNotFound:
            raise ValueError("Sheet1 not found in the Google Sheet.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while adding data: {str(e)}")
