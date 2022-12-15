import yaml
import numbers

class AppConfig:
    def __init__(self, config_file):
        self.data = yaml.safe_load(open(config_file))
        self.width = self.__get_value('width', 800)
        self.height = self.__get_value('height', 600)
        self.framerate = self.__get_value('framerate', 144)
        self.update_rate = self.__get_value('update_rate', 500)
        self.wall_aware = self.__get_value('wall_aware', 50)
        self.dt_factor = self.__get_value('dt_factor', 50)
        self.dt = self.dt_factor / self.update_rate

    def __get_value(self, key, default):
        value = self.data.get(key, default)
        if not isinstance(value, numbers.Number):
            value = default
        return value
