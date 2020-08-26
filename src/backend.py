from src.config import Config


class Backend:
    def __init__(self):
        self.config = Config()

    def get(self):
        return 5