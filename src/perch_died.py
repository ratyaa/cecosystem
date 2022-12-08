import perch

class PerchDied(perch.Perch):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Died']
        self.new_condition = ['Died']

    def _move(self):
        pass

    def activity(self):
        pass

    def observe(self,other_entities):
        pass

    def _check_walls(self):
        pass