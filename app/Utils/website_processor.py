from app.Utils.api_Mapping import WEBSITE_APIS
from app.Utils.config import get_google_sheet
from app.google_sheets.handlers.google_sheets_handler import GoogleSheetsHandler
from flask import current_app


def select_api(api, keyword):

    with current_app.test_request_context(
        json={"keyword": keyword},
        headers={"Content-Type": "application/json"}
    ):
        response = api()

        if isinstance(response, tuple):
            response_data, status_code = response
            if hasattr(response_data, "get_json"):
                return response_data.get_json(), status_code
            return response_data, status_code

        if hasattr(response, "get_json"):
            return response.get_json()

        return response


def process_websites(keyword):
    results = {}

    # Add keyword to Sheet1
    try:
        sheets_handler = GoogleSheetsHandler(get_google_sheet())
        results["sheet1"] = sheets_handler.add_input(keyword)
    except Exception as e:
        results["sheet1"] = {"error": str(e)}

    # Process 'ASOS' and 'Alibaba'
    for site in ["asos", "alibaba"]:
        try:
            api_response = select_api(WEBSITE_APIS[site], keyword)
            if isinstance(api_response, tuple):
                api_response, status_code = api_response
                results[site] = api_response
            else:
                results[site] = api_response
        except Exception as e:
            results[site] = {"error": str(e)}

    # Process 'YouTube'
    try:
        api_response = select_api(WEBSITE_APIS["youtube"], keyword)
        if isinstance(api_response, tuple):
            api_response, status_code = api_response
            results["youtube"] = api_response
        else:
            results["youtube"] = api_response
    except Exception as e:
        results["youtube"] = {"error": str(e)}

    return results
