"""Summary: Project Blueprints

Organize all root blueprints to easily allow child blueprints to be added to them.
"""
from flask import Blueprint
from app.google_sheets.google_sheets_controller import google_sheets_api

# Define the root blueprint
raw_badgerdevs_api = Blueprint('badgerdevs_api', __name__, url_prefix='/api/badgerdevs')

# Register the Google Sheets API blueprint
raw_badgerdevs_api.register_blueprint(google_sheets_api)

# Expose the main blueprint
badgerdevs_api = raw_badgerdevs_api
