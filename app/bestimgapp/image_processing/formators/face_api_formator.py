from typing import List

from azure.cognitiveservices.vision.face.models import DetectedFace, GroupResult

from ..image.image import ProcessedImage
from ..group.group import ProccesedGroup
from .base_formator import BaseFormator
from . import Source


class FaceApiFormator(BaseFormator):
    src = Source.FACE_API

    def get_proccessed_image(
        self,
        img_src,
        img_location,
        detected_faces: List[DetectedFace]
    ) -> ProcessedImage:
        if not detected_faces:
            return ProcessedImage(
                img_src=img_src,
                img_location=img_location,
                num_of_faces=0,
            )
        return ProcessedImage(
            img_src=img_src,
            img_location=img_location,
            num_of_faces=len(detected_faces),
            face_ids={f.face_id for f in detected_faces},
            face_ids_to_size={f.face_id: self._face_size(f)
                              for f in detected_faces},
        )

    def get_proccessed_group(
        self,
        g_result: GroupResult
    ) -> ProccesedGroup:
        return ProccesedGroup(
            groups=g_result.groups,
            messy_group=g_result.messy_group,
        )

    @staticmethod
    def _face_size(face: DetectedFace) -> int:
        # TODO: maybe errors can occur (further knowledge with api will tell)
        face_rec = face.face_rectangle
        return (face_rec.height + face_rec.width) // 2
