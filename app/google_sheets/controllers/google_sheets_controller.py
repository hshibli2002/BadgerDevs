from flask import Blueprint, jsonify, request

from app.Utils.website_processor import process_websites, select_api, WEBSITE_APIS

google_sheets_api = Blueprint("google_sheets", __name__, url_prefix="/google-sheets/")


@google_sheets_api.route("/input", methods=["POST"])
def add_user_input():
    """
    `POST` request using keyword parameter to store the user input in Google Sheets and
    search for products on Asos, Alibaba, and YouTube based on the website parameter.

    :return: JSON response with a message detailing the success or failure of the operation.
    """
    data = request.get_json()

    # Validate input
    if not data or "keyword" not in data:
        return jsonify({"error": "Keyword is required"}), 400

    keyword = data["keyword"]
    website = data.get("website", "").lower()

    try:
        if not website:
            results = process_websites(keyword)
        elif website in WEBSITE_APIS:
            results = {website: select_api(WEBSITE_APIS[website], keyword)}
        else:
            return jsonify({"error": f"Invalid website choice: {website}"}), 400

        return jsonify({"message": "Data successfully processed", "results": results}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
