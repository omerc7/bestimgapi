import itertools
from typing import List

from image_processing.face_wrapper import FaceClientWrapper
from .mappers import face_id_to_img
from .filters import largest_face_in
from .errors import NoFacesDetected


def get_best_image(urls: List[str]) -> str:
    face_client = FaceClientWrapper()
    imgs = face_client.detect_faces_multi(urls)
    face_ids = list(
        itertools.chain.from_iterable([img.face_ids for img in imgs]))
    if not face_ids:
        raise NoFacesDetected
    id_to_img = face_id_to_img(imgs)
    group = face_client.face_group(face_ids)
    largest_group = group.largest_group
    imgs_with_most_common = {
        face_id: img
        for face_id, img in id_to_img.items()
        if face_id in largest_group
    }
    best_img = largest_face_in(imgs_with_most_common)
    return best_img.img_location
