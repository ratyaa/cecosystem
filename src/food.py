import entity


class Food(entity.Entity):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Pike', 'Resting']
        self.new_condition = ['Pike', 'Resting']

    def _check_walls(self):
        pass

    def _move(self):
        pass

    def activity(self):
        pass

    def _search_for_food(self):
        pass

    def observe(self, other_entities):
        pass
