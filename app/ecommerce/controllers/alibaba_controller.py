from flask import Blueprint, jsonify, request
from app.ecommerce.handlers.alibaba_handler import fetch_alibaba_products
from app.google_sheets.handlers.google_sheets_handler import GoogleSheetsHandler
from app.Utils.config import get_google_sheet
from app.Utils.formattingData import format_product_data

alibaba_api = Blueprint("alibaba_api", __name__, url_prefix="/alibaba")


@alibaba_api.route("/search", methods=["POST"])
def search_and_store_products():
    """
    `POST` request using keyword parameter to search for products on Alibaba and store the data in Google Sheets.
    :return: JSON response with a message detailing the success or failure of the operation.
    """
    data = request.get_json()
    keyword = data.get("keyword")

    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    try:
        products = fetch_alibaba_products(keyword)
        formatted_data = format_product_data(products)

        sheets_handler = GoogleSheetsHandler(get_google_sheet())
        sheets_handler.add_ecommerce_data(formatted_data)

        return jsonify({"message": "Data successfully stored in Google Sheets"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
