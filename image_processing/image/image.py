from enum import Enum
from typing import Dict, Set, Union
from dataclasses import dataclass, field

from ..types import FaceId


class ImgSrc(Enum):
    URL = 'url'
    File = 'file'


@dataclass
class ProcessedImage:
    img_src: ImgSrc
    img_location: str
    num_of_faces: int
    face_ids: Union[Set[FaceId], Set] = field(default_factory=set)
    face_ids_to_size: Union[Dict[str, int], Dict] = field(default_factory=dict)

    def __bool__(self) -> bool:
        """ returns True if faces detected in image
        """
        return bool(self.num_of_faces)
