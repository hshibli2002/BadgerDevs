from flask import Blueprint

from app.ecommerce_scrappers.asos_controller import asos_api
from app.google_sheets.google_sheets_controller import google_sheets_api
from app.ecommerce_scrappers.alibaba_controller import alibaba_api

# Root blueprint
raw_badgerdevs_api = Blueprint('badgerdevs_api', __name__, url_prefix='/api/badgerdevs')

# Registering the API blueprints
raw_badgerdevs_api.register_blueprint(google_sheets_api)
raw_badgerdevs_api.register_blueprint(alibaba_api)
raw_badgerdevs_api.register_blueprint(asos_api)

badgerdevs_api = raw_badgerdevs_api
