import requests
from src.config import Config
from src.resources.album import Album
from src.resources.photo import Photo


class Backend:
    def __init__(self):
        self.config = Config()
        api = self.config.api_url()

        self.photos_url = "{}/photos".format(api)
        self.albums_url = "{}/albums".format(api)

    def __parse_albums(self, raw_response):
        return [Album(r) for r in raw_response]

    def __parse_photos(self, raw_response):
        return [Photo(r) for r in raw_response]

    def get_albums(self):
        raw_response = requests.get(self.albums_url).json()
        return self.__parse_albums(raw_response)

    def get_all_photos(self):
        raw_response = requests.get(self.photos_url).json()
        return self.__parse_photos(raw_response)

    def get_photo_album(self, album_id):
        raw_response = requests.get(self.photos_url, params={"albumId": album_id}).json()
        return self.__parse_photos(raw_response)

