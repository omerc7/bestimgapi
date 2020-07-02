import logging
import logging.config
from logging.handlers import RotatingFileHandler
# from logging.config import dictConfig

from flask import Flask, request, abort

from business_logic.errors import NoFacesDetected
from business_logic.best_image import get_best_image
from image_processing.validators import validate_image_urls
from settings import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)


app = Flask('BestImgAPI')

log = logging.getLogger(__name__)


@app.route('/best_image', methods=['POST'], endpoint='best_image')
def best_image():
    img_urls = request.args.get('imgs', None)
    if not img_urls:
        abort(400, {'message': 'no img urls provided'})
    img_urls = img_urls.split(',')
    if not validate_image_urls(img_urls):
        msg = f'imgs urls not valid, img_urls: {img_urls}'
        log.info(msg)
        abort(400, {'message': msg})
    try:
        return get_best_image(img_urls)
    except NoFacesDetected:
        abort(400, {'message': 'No Faces Detected'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
