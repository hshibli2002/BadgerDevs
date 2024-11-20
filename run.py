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
