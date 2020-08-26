from configparser import ConfigParser


class Config:
    def __init__(self, file_path='config.ini'):
        self.config = ConfigParser()
        assert file_path in self.config.read(file_path),\
            "Unable to find specified configuration file: {}.".format(file_path)

    def api_url(self):
        return self.config.get('backend', 'api_url')
