import food
import food_resting
import food_died


class FoodEscaping(food.Food):
    def __init__(self, pos, v, r, sprite, hunter):
        self.pos = pos
        self.v = v
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Food', 'Escaping']
        self.new_condition = ['Food', 'Escaping']
        self.hunter = hunter
        self.distance_x = self.hunter.pos.x - self.pos.x
        self.distance_y = self.hunter.pos.y - self.pos.y
        self.distance = (self.distance_x ** 2 + self.distance_y ** 2) ** 0.5

    def _move(self):
        pass

    def activity(self):
        pass

    def _check_walls(self):
        pass

    def _look_for_hunters(self, other_entities):
        self.distance_x = self.hunter.pos.x - self.pos.x
        self.distance_y = self.hunter.pos.y - self.pos.y
        self.distance = (self.distance_x ** 2 + self.distance_y ** 2) ** 0.5
        if self.distance >= 200:
            self.new_condition = ['Food', 'Resting']
        elif self.distance <= (self.hunter.r - self.r):
            self.new_condition = ['Food', 'Died']
        for entity in other_entities:
            if entity.start_condition[0] == 'Perch':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance <= self.distance / 2:
                    self.hunter = entity
                    self.distance = distance

    def _change_condition(self):
        if self.new_condition[1] == 'Resting':
            return food_resting.FoodResting(self.pos, self.v, self.r, (0, 255, 0))
        if self.new_condition[1] == 'Died':
            return food_died.FoodDied(self.pos * 1000, self.v, 0, self.sprite)

    def observe(self, other_entities):
        pass