from flask import Blueprint, request, jsonify

from app.Utils.config import get_google_sheet
from app.Utils.formattingData import format_product_data
from app.ecommerce.handlers.asos_handler import fetch_asos_products
from app.google_sheets.handlers.google_sheets_handler import GoogleSheetsHandler

asos_api = Blueprint("asos_api", __name__, url_prefix="/asos")


@asos_api.route("/search", methods=["POST"])
def search_and_store_products():
    data = request.get_json()
    keyword = data.get("keyword")

    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    try:
        products = fetch_asos_products(keyword)
        formatted_data = format_product_data(products)

        sheets_handler = GoogleSheetsHandler(get_google_sheet())
        sheets_handler.add_ecommerce_data(formatted_data)

        return jsonify({"message": "Asos Data successfully stored in Google Sheets"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
