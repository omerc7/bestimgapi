from typing import Iterable

import pytest

from ..validators_url import (
    validate_image_url,
    validate_image_urls,
)


@pytest.mark.parametrize(
    'url, is_valid',
    [
        ('https://s.hs-data.com/bilder/spieler/gross/13029.jpg', True),
        ('https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg', True),
        ('https://s.hs-data.com/bilder/spieler/gross/13029.jpgg', False),
        pytest.param('https://static01.nyt.com/images/2019/11/15/us/politics/15obama-abrams/'
                     'merlin_163543902_077e4a4e-e58b-43f4-89f3-4602c2aa6e64-articleLarge.jpg?quality=75&auto=webp&disable=upscale', True,
                     id='query_params'),
        pytest.param('https://static01.nyt.com/images/2019/11/15/us/politics/15obama-abrams/'
                     'merlin_163543902_077e4a4e-e58b-43f4-89f3-4602c2aa6e64-articleLarge.notpic?quality=75&auto=webp&disable=upscale', False,
                     id='query_params_false'),
        ('https://s.hs-data.com/bilder/spieler/gross/13029', False),
        ('https://s.hs-data.com/bilder/spieler/gross/13029.png', True),
    ]
)
def test_validate_image_url(url: str, is_valid: bool):
    assert validate_image_url(url) is is_valid


@pytest.mark.parametrize(
    'urls, is_valid',
    [
        ([
            'https://s.hs-data.com/bilder/spieler/gross/13029.jpg',
            'https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg',
            'https://s.hs-data.com/bilder/spieler/gross/13029.jpgg',
        ],
            False),
        ([
            'https://s.hs-data.com/bilder/spieler/gross/13029.jpg',
            'https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg',
            'https://s.hs-data.com/bilder/spieler/gross/13029.jpg',
        ],
            True),
        (['https://s.hs-data.com/bilder/spieler/gross/13029'], False),
        (['https://s.hs-data.com/bilder/spieler/gross/13029.png'], True),
    ]
)
def test_validate_images_urls(urls: Iterable[str], is_valid: bool):
    assert validate_image_urls(urls) is is_valid
