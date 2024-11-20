import gspread


class GoogleSheetsHandler:
    def __init__(self, sheet):
        self.sheet = sheet

    def get_worksheet_data(self, worksheet_name):
        """
        Fetch all data from a worksheet in the Google Sheet.

        :param worksheet_name: Name of the worksheet to fetch data from.

        :return: List of dictionaries containing the data from the worksheet.
        """
        try:
            worksheet = self.sheet.worksheet(worksheet_name)
            data = worksheet.get_all_records()
            return data
        except gspread.WorksheetNotFound:
            raise ValueError(f"Worksheet '{worksheet_name}' not found in Google Sheet '{self.sheet.title}'.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while fetching data: {str(e)}")

    def add_input(self, keyword):
        """
        Add a keyword to the Google Sheet.

        :param keyword: Keyword to add to the Google Sheet.

        :return: Dictionary containing the status and message of the operation.
        """
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

    def add_ecommerce_data(self, data):
        """
        Add ecommerce data to the Google Sheet.

        :param data: List of dictionaries containing the ecommerce data to add to the Google Sheet.
        """
        worksheet = self.sheet.worksheet("Sheet2")
        worksheet.append_rows(data, value_input_option="USER_ENTERED")

    def add_youtube_data(self, data):
        """
        Add YouTube data to the Google Sheet.

        :param data: List of dictionaries containing the YouTube data to add to the Google Sheet.
        """
        worksheet = self.sheet.worksheet("Sheet3")
        worksheet.append_rows(data, value_input_option="USER_ENTERED")
