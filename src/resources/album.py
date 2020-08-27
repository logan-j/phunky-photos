import json


class Album(object):
    def __init__(self, data):
        obj = json.loads(data)
        self.__dict__ = obj

        self.userId = obj.get("userId")
        self.id = obj.get("id")
        self.title = obj.get("title")
