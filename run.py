from flask import Flask
from app.routes.blueprints import badgerdevs_api


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(badgerdevs_api)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
