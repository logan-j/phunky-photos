import json


class Photo(object):
    def __init__(self, data):
        obj = json.loads(data)
        self.__dict__ = obj

        self.albumId = obj.get("albumId")
        self.id = obj.get("id")
        self.title = obj.get("title")
        self.url = obj.get("url")
        self.thumbnailUrl = obj.get("thumbnailUrl")
