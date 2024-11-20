from flask import Blueprint, request, jsonify

from app.Utils.config import get_google_sheet
from app.Utils.formattingData import format_youtube_data
from app.google_sheets.handlers.google_sheets_handler import GoogleSheetsHandler
from app.streaming.handlers.youtube_api_handler import youtube_metadata_search

youtube_api = Blueprint("youtube-api", __name__, url_prefix="/youtube")


@youtube_api.route("/search", methods=["POST"])
def search_youtube():
    data = request.get_json()
    keyword = data.get("keyword")

    if not keyword:
        return {"error": "Keyword parameter is required"}, 400

    max_results = request.args.get("max_results", 25)

    try:
        video_metadata = youtube_metadata_search(keyword, max_results)
        formatted_data = format_youtube_data(video_metadata)

        sheets_handler = GoogleSheetsHandler(get_google_sheet())
        sheets_handler.add_youtube_data(formatted_data)

        return jsonify({"message": "Youtube Data successfully stored in Google Sheets"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
