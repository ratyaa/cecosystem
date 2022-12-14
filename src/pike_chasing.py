import pike
import pike_resting
import pike_died
import coord

class PikeChasing(pike.Pike):
    def __init__(self, app, pos, v, r, sprite, victim, saturation, a_factor):
        self.app = app
        
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = a_factor
        self.start_condition = ['Pike','Chasing']
        self.new_condition = ['Pike','Chasing']
        self.victim = victim
        self.distance_x = self.victim.pos.x - self.pos.x
        self.distance_y = self.victim.pos.y - self.pos.y
        self.distance = (self.distance_x**2 + self.distance_y**2)**0.5
        self.saturation = saturation
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()


    def _move(self):
        self.a.x += 500*(self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
                    + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - self.__config_get('width')))
        self.a.y += 500*(self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
                    + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - self.__config_get('height')))

        self.a.x += 0.05*self.acceleration_factor*self.distance_x/self.distance
        self.a.y += 0.05*self.acceleration_factor*self.distance_y/self.distance

        self.a.x += 0.05 * self.acceleration_factor * self.v.x / (self.v.x ** 2 + self.v.y ** 2) ** 0.5
        self.a.y += 0.05 * self.acceleration_factor * self.v.y / (self.v.x ** 2 + self.v.y ** 2) ** 0.5

        self.a -= self.v

        self.v += self.a * self.__config_get('dt')
        self.pos += self.v * self.__config_get('dt')

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()
        self.saturation -= self.__config_get('dt') * self.__config_get('pike_starvation_rate')
        if self.acceleration_factor <= 5000:
            self.acceleration_factor += 0.5

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

    def _choosing_victim(self, other_entities):
        self.distance_x = self.victim.pos.x - self.pos.x
        self.distance_y = self.victim.pos.y - self.pos.y
        self.distance = (self.distance_x ** 2 + self.distance_y ** 2) ** 0.5
        if self.distance >= 100:
            self.new_condition = ['Pike', 'Resting']
        elif self.distance <= (self.r - self.victim.r):
            self.saturation += 500
            self.acceleration_factor -= 30
            self.new_condition = ['Pike', 'Resting']
        if self.victim.new_condition == ['Perch', 'Died']:
            self.new_condition = ['Pike', 'Resting']
        for entity in other_entities:
            if entity.start_condition[0] == 'Perch':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance <= self.distance/2:
                    self.victim = entity
                    self.distance = distance
        if self.saturation <= 0:
            self.new_condition = ['Pike', 'Died']


    def _change_condition(self):
        if self.new_condition[1] == 'Resting':
            return pike_resting.PikeResting(self.app, self.pos, self.v,self.r,(255,0,0),self.saturation, self.acceleration_factor)
        if self.new_condition[1] == 'Died':
            return pike_died.PikeDied(self.app, self.pos, self.v, self.r, (100, 0, 0))


    def observe(self,other_entities):
        self._check_walls()
        self._choosing_victim(other_entities)
        self.distance_x = self.victim.pos.x - self.pos.x
        self.distance_y = self.victim.pos.y - self.pos.y
