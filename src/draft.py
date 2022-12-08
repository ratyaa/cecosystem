if self.pos.x - self.r <= 0 or self.pos.x + self.r >= app_config.WIDTH:
    self.v.x = -self.v.x
if self.pos.y - self.r <= 0 or self.pos.x + self.r >= app_config.HEIGHT:
    self.v.y = -self.v.y