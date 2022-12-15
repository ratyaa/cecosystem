import pike
import app_config
import coord

class PikeDied(pike.Pike):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.a = coord.Coord(0,0)
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Entity', 'Died']
        self.new_condition = ['Entity', 'Died']

    def _move(self):
        self.a -= self.v
        self.v += self.a* app_config.dt
        if (self.pos.x - app_config.WALL_AWARE <= 0) or (self.pos.x + self.r + app_config.WALL_AWARE >= app_config.WIDTH):
            self.v.x = -self.v.x
        if (self.pos.y - app_config.WALL_AWARE <= 0) or (self.pos.y + self.r + app_config.WALL_AWARE >= app_config.HEIGHT):
            self.v.y = -self.v.y
        self.pos += self.v * app_config.dt


    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._check_walls()
        self._move()

    def observe(self,other_entities):
        pass

    def _check_walls(self):
           pass