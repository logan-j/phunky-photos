import requests
from src.backend import Backend


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'https://jsonplaceholder.typicode.com/photos':
        if 'params' in kwargs:
            album_id = kwargs['params']['albumId']
            return MockResponse([{"albumId": album_id,
                                  "id": album_id,
                                  "title": "accusamus beatae ad facilis cum similique qui sunt",
                                  "url": "https://via.placeholder.com/600/92c952",
                                  "thumbnailUrl": "https://via.placeholder.com/150/92c952"}], 200)

        return MockResponse([{"albumId": 1,
                              "id": 1,
                              "title": "accusamus beatae ad facilis cum similique qui sunt",
                              "url": "https://via.placeholder.com/600/92c952",
                              "thumbnailUrl": "https://via.placeholder.com/150/92c952"}], 200)

    elif args[0] == 'https://jsonplaceholder.typicode.com/albums':
        return MockResponse([{"userId": 1,
                              "id": 1,
                              "title": "quidem molestiae enim"}], 200)

    return MockResponse(None, 404)


def test_get_albums(monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_requests_get)
    backend = Backend()
    album = backend.get_albums()[0]
    assert album.userId == 1
    assert album.id == 1
    assert album.title == "quidem molestiae enim"


def test_get_all_photos(monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_requests_get)
    backend = Backend()
    album = backend.get_all_photos()[0]
    assert album.albumId == 1
    assert album.id == 1
    assert album.title == "accusamus beatae ad facilis cum similique qui sunt"
    assert album.url == "https://via.placeholder.com/600/92c952"
    assert album.thumbnailUrl == "https://via.placeholder.com/150/92c952"


def test_get_one_album(monkeypatch):
    monkeypatch.setattr(requests, 'get', mocked_requests_get)
    backend = Backend()
    album = backend.get_photo_album(3)[0]
    assert album.albumId == 3
    assert album.id == 3
    assert album.title == "accusamus beatae ad facilis cum similique qui sunt"
    assert album.url == "https://via.placeholder.com/600/92c952"
    assert album.thumbnailUrl == "https://via.placeholder.com/150/92c952"
