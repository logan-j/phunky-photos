import json


class Photo(object):
    def __init__(self, data):
        self.__dict__ = data

        self.albumId = data.get("albumId")
        self.id = data.get("id")
        self.title = data.get("title")
        self.url = data.get("url")
        self.thumbnailUrl = data.get("thumbnailUrl")
