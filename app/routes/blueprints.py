"""Summary
In this snippet, we are creating a blueprint that will be used to register all the API blueprints.
The purpose of this blueprint is to group all the API endpoints under a common URL prefix.
This allows us to organize our API endpoints in a structured way and make it easier to manage and maintain them.
"""

from flask import Blueprint

from app.ecommerce.controllers.asos_controller import asos_api
from app.google_sheets.controllers.google_sheets_controller import google_sheets_api
from app.ecommerce.controllers.alibaba_controller import alibaba_api
from app.streaming.controllers.youtube_api_controller import youtube_api

# Root blueprint
raw_badgerdevs_api = Blueprint('badgerdevs_api', __name__, url_prefix='/api/badgerdevs')

# Registering the API blueprints
raw_badgerdevs_api.register_blueprint(google_sheets_api)
raw_badgerdevs_api.register_blueprint(alibaba_api)
raw_badgerdevs_api.register_blueprint(asos_api)
raw_badgerdevs_api.register_blueprint(youtube_api)

badgerdevs_api = raw_badgerdevs_api
