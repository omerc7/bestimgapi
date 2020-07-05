import logging
import logging.config

from flask import Flask

from settings import LOGGING_CONFIG
from bestimgapp.bestimg import best_face_bp

logging.config.dictConfig(LOGGING_CONFIG)


def create_app() -> Flask:
    """create flask app and register blueprints"""
    app = Flask('BestImgAPI')
    app.register_blueprint(best_face_bp)

    return app


app = create_app()

if __name__ == '__main__':
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
