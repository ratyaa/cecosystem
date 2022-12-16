import pike
import coord

class PikeDied(pike.Pike):
    def __init__(self, app, pos, v, r, sprite):
        self.app = app
        
        self.pos = pos
        self.v = v
        self.a = coord.Coord(0,0)
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Entity', 'Died']
        self.new_condition = ['Entity', 'Died']
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _move(self):
        self.a -= self.v
        self.v += self.a* self.__config_get('dt')
        if (self.pos.x - self.__config_get('wall_aware') <= 0) or (self.pos.x + self.r + self.__config_get('wall_aware') >= self.__config_get('width')):
            self.v.x = -self.v.x
        if (self.pos.y - self.__config_get('wall_aware') <= 0) or (self.pos.y + self.r + self.__config_get('wall_aware') >= self.__config_get('height')):
            self.v.y = -self.v.y
        self.pos += self.v * self.__config_get('dt')


    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._check_walls()
        self._move()

    def observe(self,other_entities):
        pass

    def _check_walls(self):
           pass
