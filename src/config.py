import yaml
import numbers

import app_var

class AppConfig:
    def __init__(self, config_file_path, defaults_file_path):
        self.defaults_raw = self.__read_config(defaults_file_path)
        self.app_vars_raw = self.__read_config(config_file_path)

        self.app_vars = {}
        self.__init_vars()

    def __read_config(self, config_file_path):
        return yaml.safe_load(open(config_file_path))

    def __init_vars(self):
        for key, value in self.app_vars_raw.items():
            self.app_vars[key] = app_var.AppVariable(
                key,
                value,
                self.defaults_raw.get(key),
                self.defaults_raw.get(key).get('in_numeric', True),
            )
