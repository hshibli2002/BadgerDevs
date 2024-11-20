"""Summary:
In this snippet, we are defining the main entry point for the Flask application.
The create_app function initializes the Flask application and registers the main blueprint.
"""

from flask import Flask
from app.routes.blueprints import badgerdevs_api


def create_app():
    app = Flask(__name__)

    # Register Main Blueprint
    app.register_blueprint(badgerdevs_api)
    app.debug = True

    return app


if __name__ == '__main__':
    application = create_app()

    application.run(debug=True)
