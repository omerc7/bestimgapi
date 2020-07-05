from typing import List

from ..image_processing.face_wrapper import FaceClientWrapper
from .errors import NoFacesDetected
from .filters import largest_face_in
from .mappers import (
    face_id_to_img,
    face_ids_from_imgs,
    imgs_with_most_common_face,
)


def get_best_image(urls: List[str]) -> str:
    face_client = FaceClientWrapper()
    imgs = face_client.detect_faces_multi(urls)
    face_ids = face_ids_from_imgs(imgs)
    if not face_ids:
        raise NoFacesDetected

    id_to_img = face_id_to_img(imgs)
    if len(face_ids) == 1:
        return id_to_img[face_ids[0]].img_location

    group = face_client.face_group(face_ids)
    imgs_with_most_common = imgs_with_most_common_face(id_to_img, group)
    best_img = largest_face_in(imgs_with_most_common)
    return best_img.img_location
