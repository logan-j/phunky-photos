from src.resources.album import Album
from src.resources.photo import Photo


def test_photo_object():

    photo_json = """{"albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"}"""

    photo = Photo(photo_json)
    assert photo.albumId == 1
    assert photo.id == 1
    assert photo.title == "accusamus beatae ad facilis cum similique qui sunt"
    assert photo.url == "https://via.placeholder.com/600/92c952"
    assert photo.thumbnailUrl == "https://via.placeholder.com/150/92c952"


def test_album_object():

    album_json = """{"userId": 1,
    "id": 1,
    "title": "quidem molestiae enim"}"""

    album = Album(album_json)
    assert album.userId == 1
    assert album.id == 1
    assert album.title == "quidem molestiae enim"
