import perch
import coord
import perch_resting
import perch_died

class PerchEscaping(perch.Perch):
    def __init__(self, app, pos, v, r, sprite, hunter):
        self.app = app
        
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = 2800.0
        self.start_condition = ['Perch', 'Escaping']
        self.new_condition = ['Perch', 'Escaping']
        self.hunter = hunter
        self.distance_x = self.hunter.pos.x - self.pos.x
        self.distance_y = self.hunter.pos.y - self.pos.y
        self.distance = (self.distance_x**2 + self.distance_y**2)**0.5
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _move(self):
        self.a.x += 500*(self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
            + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - self.__config_get('width')))
        self.a.y += 500*(self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
            + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - self.__config_get('height')))

        self.a.x -= 0.05*self.acceleration_factor*self.distance_x/self.distance
        self.a.y -= 0.05*self.acceleration_factor*self.distance_y/self.distance

        self.a.x += 0.05 * self.acceleration_factor * self.v.x / (self.v.x ** 2 + self.v.y ** 2) ** 0.5
        self.a.y += 0.05 * self.acceleration_factor * self.v.y / (self.v.x ** 2 + self.v.y ** 2) ** 0.5

        self.a -= self.v

        self.v += self.a * self.__config_get('dt')

        self.pos += self.v * self.__config_get('dt')

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()

    def _check_walls(self):
        if self.pos.x < self.__config_get('wall_aware'):
            self.walls['left'] = 1
        else:
            self.walls['left'] = 0
        if self.pos.x > self.__config_get('width') - self.__config_get('wall_aware'):
            self.walls['right'] = 1
        else:
            self.walls['right'] = 0
        if self.pos.y < self.__config_get('wall_aware'):
            self.walls['top'] = 1
        else:
            self.walls['top'] = 0
        if self.pos.y > self.__config_get('height') - self.__config_get('wall_aware'):
            self.walls['bottom'] = 1
        else:
            self.walls['bottom'] = 0

    def _look_for_hunters(self,other_entities):
        self.distance_x = self.hunter.pos.x - self.pos.x;
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
            return perch_resting.PerchResting(self.app, self.pos, self.v, self.r, (0, 255, 0))
        if self.new_condition[1] == 'Died':
            return perch_died.PerchDied(self.app, self.pos*1000, self.v, 0, self.sprite)

    def observe(self, other_entities):
        self._check_walls()
        self._look_for_hunters(other_entities)
