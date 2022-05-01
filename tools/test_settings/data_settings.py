from tools import ReadFile
from patterns.singleton import Singleton

CONFIG_PATH = "tests/config.json"


class DataSettings(metaclass=Singleton):

    @staticmethod
    def config_data():
        return ReadFile.read_file(CONFIG_PATH)
