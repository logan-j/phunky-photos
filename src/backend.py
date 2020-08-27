import requests
from src.config import Config


class Backend:
    def __init__(self):
        self.config = Config()
        api = self.config.api_url()

        self.photos_url = "{}/photos".format(api)
        self.albums_url = "{}/albums".format(api)
