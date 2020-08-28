import json


class Album(object):
    def __init__(self, data):
        self.__dict__ = data

        self.userId = data.get("userId")
        self.id = data.get("id")
        self.title = data.get("title")
