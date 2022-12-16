import food
import food_escaping


class FoodResting(food.Food):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Perch', 'Resting']
        self.new_condition = ['Perch', 'Resting']
        self.new_hunter = self

    def _move(self):
        pass

    def activity(self):
        pass

    def _check_walls(self):
        pass

    def _look_for_hunters(self, other_entities):
        nearest_hunter_dist = 115
        for entity in other_entities:
            if entity.start_condition[0] == 'Perch':
                distance = ((self.pos.x - entity.pos.x) ** 2 + (self.pos.y - entity.pos.y) ** 2) ** 0.5
                if distance < nearest_hunter_dist:
                    nearest_hunter_dist = distance
                    self.new_condition = ['Food', 'Escaping']
                    self.new_hunter = entity

    def _change_condition(self):
        if self.new_condition[1] == 'Escaping':
            return food_escaping.FoodEscaping(self.pos, self.v, self.r, (255, 255, 255), self.new_hunter)

    def observe(self, other_entities):
        pass