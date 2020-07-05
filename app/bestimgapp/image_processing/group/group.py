from typing import List, Union
from dataclasses import dataclass

from ..types import FaceId


@dataclass
class ProccesedGroup:
    groups: List[List[FaceId]]
    messy_group: List[FaceId]
    cashed_largest_groups: Union[List[FaceId], None] = None

    @property
    def largest_group(self):
        """ Does not include messy group"""
        if not self.cashed_largest_groups:
            self.cashed_largest_groups = max(self.groups, key=len)
        return self.cashed_largest_groups
