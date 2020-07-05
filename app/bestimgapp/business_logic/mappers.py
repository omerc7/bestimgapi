import itertools

from typing import List, Dict

from ..image_processing.image.image import ProcessedImage
from ..image_processing.group.group import ProccesedGroup
from ..image_processing.types import FaceId


def face_ids_from_imgs(imgs: List[ProcessedImage]) -> List[FaceId]:
    return list(
        itertools.chain.from_iterable([img.face_ids for img in imgs]))


def face_id_to_img(imgs: List[ProcessedImage]) -> Dict[FaceId, ProcessedImage]:
    return {face_id: img for img in imgs for face_id in img.face_ids}


def imgs_with_most_common_face(
        id_to_img: Dict[FaceId, ProcessedImage],
        groups: ProccesedGroup) -> Dict[FaceId, ProcessedImage]:
    """return images with most common face"""
    largest_group = groups.largest_group
    return {
        face_id: img
        for face_id, img in id_to_img.items()
        if face_id in largest_group
    }
