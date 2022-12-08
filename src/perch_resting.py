import perch
import perch_escaping
import coord
import app_config

class PerchResting(perch.Perch):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = 1000.0
        self.start_condition = ['Perch', 'Resting']
        self.new_condition = ['Perch', 'Resting']
        self.new_hunter = self


    def _move(self):
        self.a.x += 1000*self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
            + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - app_config.WIDTH)
        self.a.y += 1000*self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
            + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - app_config.HEIGHT)

        self.v += self.a * app_config.dt

        self.pos += self.v * app_config.dt

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()

    def _check_walls(self):
        if self.pos.x < app_config.WALL_AWARE:
            self.walls['left'] = 1
        else:
            self.walls['left'] = 0
        if self.pos.x > app_config.WIDTH - app_config.WALL_AWARE:
            self.walls['right'] = 1
        else:
            self.walls['right'] = 0
        if self.pos.y < app_config.WALL_AWARE:
            self.walls['top'] = 1
        else:
            self.walls['top'] = 0
        if self.pos.y > app_config.HEIGHT - app_config.WALL_AWARE:
            self.walls['bottom'] = 1
        else:
            self.walls['bottom'] = 0

    def _look_for_hunters(self,other_entities):
        for entity in other_entities:
            distance = ((self.pos.x - entity.pos.x)**2 + (self.pos.y - entity.pos.y)**2)**0.5
            if entity.start_condition[0] == 'Pike' and distance <= self.r + entity.r + 30:
                self.new_condition = ['Pike', 'Escaping']
                self.new_hunter = entity

    def _change_condition(self):
        if self.new_condition[1] == 'Escaping':
            return perch_escaping.PerchEscaping(self.pos, self.v, self.r, self.sprite, self.new_hunter)

    def observe(self,other_entities):
        self._check_walls()
        self._look_for_hunters(other_entities)
    
    
