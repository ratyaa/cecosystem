import perch
import coord

class PerchResting(perch.Perch):
    def __init__(self, pos, v, r, sprite):
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite

    def _move(self):
        self.a.x += ((50 / (self.pos.x - self.r) + 50 / (self.pos.x + self.r - 800))) * 0.000001
        self.a.y += ((50 / (self.pos.y - self.r) + 50 / (self.pos.y + self.r - 600))) * 0.000001

        self.v.x += self.a.x
        self.v.y += self.a.y

        self.pos.x += self.v.x
        self.pos.y += self.v.y

    def activity(self):
        self._move()

    def observe(self):
        pass
    
    
