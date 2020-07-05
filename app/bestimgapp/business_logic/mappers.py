from typing import List, Dict

from ..image_processing.image.image import ProcessedImage
from ..image_processing.types import FaceId


def face_id_to_img(imgs: List[ProcessedImage]) -> Dict[FaceId, ProcessedImage]:
    # optional caching
    return {face_id: img for img in imgs for face_id in img.face_ids}
