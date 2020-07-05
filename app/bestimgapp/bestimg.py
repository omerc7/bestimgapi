import logging

from flask import Blueprint, request, abort

from .business_logic.errors import NoFacesDetected
from .business_logic.best_image import get_best_image
from .validators import validators_url


log = logging.getLogger(__name__)


best_face_bp = Blueprint('best_image', __name__, url_prefix='/best_image')


@best_face_bp.route('/best_face_image', methods=['GET'], endpoint='best_face_image')
def best_face_image():
    img_urls = request.args.get('imgs', None)
    if not img_urls:
        abort(400, {'message': 'no img urls provided'})
    img_urls = img_urls.split(',')
    if not validators_url.validate_image_urls(img_urls):
        msg = f'imgs urls not valid, img_urls: {img_urls}'
        log.info(msg)
        abort(400, {'message': msg})
    try:
        return get_best_image(img_urls)
    except NoFacesDetected:
        abort(400, {'message': 'No Faces Detected'})
