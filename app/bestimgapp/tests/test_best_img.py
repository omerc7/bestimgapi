import pytest

from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_best_image_working_mj(client):
    imgs = ','.join([
        'https://usatftw.files.wordpress.com/2020/04/jordan-3.jpg',
        'https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg',
        'https://image-cdn.essentiallysports.com/wp-content/uploads/20200420111658/SP-MJ.jpeg',
    ])
    response = client.get(f'/best_image/best_face_image?imgs={imgs}')
    assert response.get_data(
    ).decode("utf-8") == 'https://image-cdn.essentiallysports.com/wp-content/uploads/20200420111658/SP-MJ.jpeg'


def test_best_with_image_ronaldo(client):
    imgs = ','.join([
        'https://s.hs-data.com/bilder/spieler/gross/13029.jpg',
        'https://www.insidesport.co/wp-content/uploads/2018/05/1-16-696x464.jpg',
        'https://i0.wp.com/sportytell.com/wp-content/uploads/2018/11/cristiano-ronaldo-juventus.jpg',
        'https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg',
        'https://as01.epimg.net/en/imagenes/2019/12/11/football/1576102825_947330_noticia_normal.jpg',
    ])
    response = client.get(f'/best_image/best_face_image?imgs={imgs}')
    assert response.get_data(
    ).decode("utf-8") == 'https://i0.wp.com/sportytell.com/wp-content/uploads/2018/11/cristiano-ronaldo-juventus.jpg'


def test_best_image_working_one_img(client):
    """Test working with only one image with a face"""
    imgs = ','.join([
        'https://usatftw.files.wordpress.com/2020/04/jordan-3.jpg',
    ])
    response = client.get(f'/best_image/best_face_image?imgs={imgs}')
    assert response.get_data(
    ).decode("utf-8") == 'https://usatftw.files.wordpress.com/2020/04/jordan-3.jpg'


def test_best_with_image_no_faces(client):
    imgs = ','.join([
        'https://static.scientificamerican.com/sciam/cache/file/4E0744CD-793A-4EF8-B550B54F7F2C4406_source.jpg',
        'upload.wikimedia.org/wikipedia/commons/thumb/4/42/Shaqi_jrvej.jpg/250px-Shaqi_jrvej.jpg',
    ])
    response = client.get(f'/best_image/best_face_image?imgs={imgs}')
    assert response.status == '400 BAD REQUEST'
