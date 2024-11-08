from flask import Blueprint, jsonify, request
from app.google_sheets.google_sheets_handler import GoogleSheetsHandler

google_sheets_api = Blueprint("google_sheets", __name__, url_prefix="/google-sheets/")


@google_sheets_api.route("/get-worksheet-data", methods=["GET"])
def get_worksheet_data():
    sheet_name = request.args.get("sheet_name")
    worksheet_name = request.args.get("worksheet_name")
    try:
        sheets_handler = GoogleSheetsHandler(sheet_name)
        data = sheets_handler.get_worksheet_data(worksheet_name)
        return jsonify({"data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
