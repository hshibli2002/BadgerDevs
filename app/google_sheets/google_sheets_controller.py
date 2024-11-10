from flask import Blueprint, jsonify, request
from app.google_sheets.google_sheets_handler import GoogleSheetsHandler
from app.Utils.config import get_google_sheet

google_sheets_api = Blueprint("google_sheets", __name__, url_prefix="/google-sheets/")


@google_sheets_api.route("/get-worksheet-data", methods=["GET"])
def get_worksheet_data():
    worksheet_name = request.args.get("worksheet_name")
    try:
        sheet = get_google_sheet()
        sheets_handler = GoogleSheetsHandler(sheet)

        data = sheets_handler.get_worksheet_data(worksheet_name)
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@google_sheets_api.route("/add-user-input", methods=["POST"])
def add_user_input():
    data = request.get_json()

    if not data or 'keyword' not in data:
        return jsonify({"error": "Keyword not provided"}), 400

    keyword = data['keyword']
    try:
        sheet = get_google_sheet()
        sheets_handler = GoogleSheetsHandler(sheet)

        result = sheets_handler.add_user_input(keyword)
        if result["status"] == "exists":
            return jsonify({"message": result["message"]}), 200
        else:
            return jsonify({"message": result["message"]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
