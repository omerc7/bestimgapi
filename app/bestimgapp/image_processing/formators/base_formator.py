from typing import Type
from abc import ABC, abstractstaticmethod, abstractmethod

from .source import Source


_formators = {}


def get_formator(src: Source) -> Type['BaseFormator']:
    """Return the formator class requested

    :raise: KeyError if src formator not in _formators,
            needs to derive from BaseFormator to subscribe via __subclass_init__ 
    :return: class of Formator requested
    """
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
