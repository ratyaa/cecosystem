from abc import abstractmethod
import entity

class Perch(entity.Entity):
    def __init__(self, app, pos, v, r, sprite):
        self.app = app
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _move(self):
        pass

    def activity(self):
        pass

    def observe(self):
        pass

    def _check_walls(self, pos):
        walls = {}
        if pos.x < self.__config_get('wall_aware'):
            walls['left'] = 1
        else:
            walls['left'] = 0
        if pos.x > self.__config_get('width') - self.__config_get('wall_aware'):
            walls['right'] = 1
        else:
            walls['right'] = 0
        if pos.y < self.__config_get('wall_aware'):
            walls['top'] = 1
        else:
            walls['top'] = 0
        if pos.y > self.__config_get('height') - self.__config_get('wall_aware'):
            walls['bottom'] = 1
        else:
            walls['bottom'] = 0

        return walls
        
