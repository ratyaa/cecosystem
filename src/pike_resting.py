import pike
import pike_chasing
import pike_died
import coord
import app_config

class PikeResting(pike.Pike):
    def __init__(self, pos, v, r, sprite, saturation = 5000, a_factor = 4000):
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = a_factor
        self.start_condition = ['Pike', 'Resting']
        self.new_condition = ['Pike', 'Resting']
        self.new_victim = self
        self.saturation = saturation
        self.division = 0

    def _move(self):
        self.a.x += 500*(self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
                    + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - app_config.WIDTH))
        self.a.y += 500*(self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
                    + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - app_config.HEIGHT))

        self.a.x += 0.05*self.acceleration_factor*self.v.x/(self.v.x**2 + self.v.y**2)**0.5
        self.a.y += 0.05*self.acceleration_factor*self.v.y/(self.v.x ** 2 + self.v.y ** 2) ** 0.5

        self.a -= self.v

        self.v += self.a * app_config.dt

        self.pos += self.v * app_config.dt

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()
        self.saturation -= 0.5
        self.acceleration_factor += 0.5

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


    def _search_for_food(self,other_entities):
        nearest_victim_dist = 90
        for entity in other_entities:
            if entity.start_condition[0] == 'Perch':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance < nearest_victim_dist:
                    nearest_victim_dist = distance
                    self.new_condition = ['Pike', 'Chasing']
                    self.new_victim = entity
        if self.saturation <= 0:
            self.new_condition = ['Pike', 'Died']

    def division_process(self):
        '''Функция реализует процесс размножения щуки'''

        if self.division >= 5000 and self.saturation >= 4000:
            self.new_condition = ['Pike', 'Division']


    def _change_condition(self):
        if self.new_condition[1] == 'Chasing':
            return pike_chasing.PikeChasing(self.pos, self.v, self.r, (255,0,0), self.new_victim, self.saturation, self.acceleration_factor)
        elif self.new_condition[1] == 'Division':
            return PikeResting(self.pos,
                               0.5*self.v + 0.5*coord.Coord(self.v.y*self.direction, -self.v.x*self.direction),
                               self.r, (255, 0, 0),
                               0.5*self.saturation)
        elif self.new_condition[1] == 'Died':
            return pike_died.PikeDied(self.pos, self.v, self.r, (100,0,0))


    def observe(self,other_entities):
        self._check_walls()
        self.division_process()
        self._search_for_food(other_entities)