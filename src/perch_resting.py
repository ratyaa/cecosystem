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
        self.division = 0
        self.direction = 1


    def _move(self):
        self.a.x += 500*(self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
            + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - app_config.WIDTH))
        self.a.y += 500*(self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
            + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - app_config.HEIGHT))

        self.a.x += 0.05 * self.acceleration_factor * self.v.x / (self.v.x ** 2 + self.v.y ** 2) ** 0.5
        self.a.y += 0.05 * self.acceleration_factor * self.v.y / (self.v.x ** 2 + self.v.y ** 2) ** 0.5

        self.a -= self.v

        self.v += self.a * app_config.dt

        self.pos += self.v * app_config.dt

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()
        self.division += 1

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

    def _look_for_hunters(self, other_entities):
        nearest_hunter_dist = 115
        for entity in other_entities:
            if entity.start_condition[0] == 'Pike':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance < nearest_hunter_dist:
                    nearest_hunter_dist = distance
                    self.new_condition = ['Perch', 'Escaping']
                    self.new_hunter = entity

    def division_process(self):
        ''''Функция реализует процесс размножения окуня'''
        if self.division >= 2500:
            self.new_condition = ['Perch', 'Division']

    def _change_condition(self):
        if self.new_condition[1] == 'Escaping':
            return perch_escaping.PerchEscaping(self.pos, self.v, self.r, (0, 255, 0), self.new_hunter)
        if self.new_condition[1] == 'Division':
            if self.direction == -1:
                self.direction = 1
            else:
                self.direction = -1
            return PerchResting(self.pos,
                                0.5*self.v + 0.5*coord.Coord(self.v.y*self.direction, -self.v.x*self.direction),
                                self.r, (0, 255, 0))

    def observe(self, other_entities):
        self._check_walls()
        self.division_process()
        self._look_for_hunters(other_entities)
    
    
