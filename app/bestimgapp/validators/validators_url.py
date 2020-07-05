from typing import Iterable
from urllib.parse import ParseResult, urlparse

from settings import VALID_IMAGE_FORMATS


def validate_url_format(parsed_url: ParseResult) -> bool:
    """ Returns True if url ends with picture format and
        url starts with https or http"""
    valid_start = parsed_url.scheme in {'https', 'http'}
    valid_end = any((
        parsed_url.path.endswith(f)
        for f in VALID_IMAGE_FORMATS
    ))
    return all((
        valid_start,
        valid_end,
    ))


def validate_image_url(url_to_validate: str) -> bool:
    """ Returns True if url is valid"""
    parsed_url = urlparse(url_to_validate)
    return all((
        validate_url_format(parsed_url),
    ))


def validate_image_urls(urls_to_validate: Iterable[str]) -> bool:
    """ Returns True if all urls are valid, else False"""
    return all((
        validate_image_url(url)
        for url in urls_to_validate
    ))
