from typing import Dict, Optional

from image_processing.image.image import ProcessedImage
from image_processing.types import FaceId


def largest_face_in(imgs_mapping=Dict[FaceId, ProcessedImage]) -> Optional[ProcessedImage]:
    """ returns pic with largest face in face_ids
    """
    largest = 0
    largest_face_img = None
    for face_id, img in imgs_mapping.items():
        if size := img.face_ids_to_size[face_id] > largest:
            largest = size
            largest_face_img = img
    return largest_face_img
