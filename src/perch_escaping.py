import perch
import coord
import app_config
import perch_resting
import perch_died

class PerchEscaping(perch.Perch):
    def __init__(self, pos, v, r, sprite, hunter):
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = 2000.0
        self.start_condition = ['Perch', 'Escaping']
        self.new_condition = ['Perch', 'Escaping']
        self.hunter = hunter
        self.distance_x = self.hunter.pos.x - self.pos.x
        self.distance_y = self.hunter.pos.y - self.pos.y
        self.distance = (self.distance_x**2 + self.distance_y**2)**0.5


    def _move(self):
        self.a.x += 500*(self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
            + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - app_config.WIDTH))
        self.a.y += 500*(self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
            + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - app_config.HEIGHT))

        self.a.x -= 0.05*self.acceleration_factor*self.distance_x/self.distance
        self.a.y -= 0.05*self.acceleration_factor*self.distance_y/self.distance

        self.a.x += 0.05 * self.acceleration_factor * self.v.x / (self.v.x ** 2 + self.v.y ** 2) ** 0.5
        self.a.y += 0.05 * self.acceleration_factor * self.v.y / (self.v.x ** 2 + self.v.y ** 2) ** 0.5

        self.a -= self.v

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
        self.distance_x = self.hunter.pos.x - self.pos.x
        self.distance_y = self.hunter.pos.y - self.pos.y
        self.distance = (self.distance_x ** 2 + self.distance_y ** 2) ** 0.5
        if self.distance >= 200:
            self.new_condition = ['Perch', 'Resting']
        elif self.distance <= (self.hunter.r - self.r):
            self.new_condition = ['Perch', 'Died']
        for entity in other_entities:
            if entity.start_condition[0] == 'Pike':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance <= self.distance/2:
                    self.hunter = entity
                    self.distance = distance


    def _change_condition(self):
        if self.new_condition[1] == 'Resting':
            return perch_resting.PerchResting(self.pos, self.v, self.r, (0, 255, 0))
        if self.new_condition[1] == 'Died':
            return perch_died.PerchDied(self.pos*1000, self.v, 0, self.sprite)

    def observe(self, other_entities):
        self._check_walls()
        self._look_for_hunters(other_entities)