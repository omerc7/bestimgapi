from typing import Type
from abc import ABC, abstractstaticmethod

from .source import Source


_formators = {}


def get_formator(src: Source) -> Type['BaseFormator']:
    # will raise KeyError if src not in _formators
    return _formators[src]


class BaseFormator(ABC):
    src = None

    @abstractstaticmethod
    def get_proccessed_image():
        raise NotImplemented

    @abstractstaticmethod
    def get_proccessed_group():
        raise NotImplemented

    @classmethod
    def __init_subclass__(cls, **kwargs):
        if not cls.src:
            raise RuntimeError(
                f'subclass of BaseFormator: {cls.__name__} must override src attribute')
        _formators[cls.src] = cls
        super().__init_subclass__(**kwargs)
