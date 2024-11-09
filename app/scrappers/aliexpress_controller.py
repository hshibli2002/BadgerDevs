from flask import Blueprint, jsonify, request
from app.scrappers.aliexpress_handler import fetch_aliexpress_products

aliexpress_api = Blueprint("aliexpress_api", __name__, url_prefix="/aliexpress")


@aliexpress_api.route("/search", methods=["GET"])
def search_products():
    keyword = request.args.get("keyword", type=str)
    page = request.args.get("page", default=1, type=int)
    sort = request.args.get("sort", default="default", type=str)

    if not keyword:
        return jsonify({"error": "Keyword parameter is required"}), 400

    try:
        products = fetch_aliexpress_products(keyword=keyword, page=page, sort=sort)
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
