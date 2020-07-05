from typing import List, Dict
from logging import getLogger

from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

from settings import FACE_API_ENDPOINT, FACE_API_KEY

from .types import FaceId
from .image.image import ProcessedImage
from .formators import get_formator, Source
from .group.group import ProccesedGroup


log = getLogger(__name__)


class FaceClientWrapper:
    def __init__(self):
        self.client = FaceClient(
            FACE_API_ENDPOINT,
            CognitiveServicesCredentials(FACE_API_KEY),
        )
        self.formator = get_formator(Source.FACE_API)()

    def detect_faces(self, url: str) -> List[ProcessedImage]:
        detected_faces = self.client.face.detect_with_url(url=url)
        return self.formator.get_proccessed_image(
            img_src='url',
            img_location=url,
            detected_faces=detected_faces,
        )

    def face_group(self, face_ids: List[FaceId]) -> ProccesedGroup:
        group = self.client.face.group(face_ids=face_ids)
        return self.formator.get_proccessed_group(group)

    def detect_faces_multi(self, urls: List[str], throw=False) -> List[ProcessedImage]:
        imgs = []
        for url in urls:
            try:
                imgs.append(self.detect_faces(url))
            except Exception as ex:
                log.warning(
                    f"Error detecting faces in url: {url}, error: {ex}")
                if throw:
                    raise
        return imgs
