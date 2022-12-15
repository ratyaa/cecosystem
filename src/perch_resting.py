import perch
import coord

class PerchResting(perch.Perch):
    def __init__(self, pos, v, r, sprite, app):
        self.app = app
        self.pos = pos
        self.v = v
        self.r = r
        self.a = coord.Coord(0, 0)
        self.sprite = sprite
        self.walls = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        self.acceleration_factor = 2000.0

    def _move(self):
        self.a.x += self.walls['left'] * (self.acceleration_factor) / (self.pos.x - self.r) \
            + self.walls['right'] * (self.acceleration_factor) / (self.pos.x + self.r - self.app.config.width)
        self.a.y += self.walls['top'] * (self.acceleration_factor) / (self.pos.y - self.r) \
            + self.walls['bottom'] * (self.acceleration_factor) / (self.pos.y + self.r - self.app.config.height)

        self.v += self.a * self.app.config.dt
        self.pos += self.v * self.app.config.dt

    def activity(self):
        self.a.x = 0
        self.a.y = 0
        self._move()

    def _check_walls(self):
        if self.pos.x < self.app.config.wall_aware:
            self.walls['left'] = 1
        else:
            self.walls['left'] = 0
        if self.pos.x > self.app.config.width - self.app.config.wall_aware:
            self.walls['right'] = 1
        else:
            self.walls['right'] = 0
        if self.pos.y < self.app.config.wall_aware:
            self.walls['top'] = 1
        else:
            self.walls['top'] = 0
        if self.pos.y > self.app.config.height - self.app.config.wall_aware:
            self.walls['bottom'] = 1
        else:
            self.walls['bottom'] = 0
            
    def observe(self):
        self._check_walls()
    
    
