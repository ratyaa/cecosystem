import perch

class PerchDied(perch.Perch):
    def __init__(self, app, pos, v, r, sprite):
        self.app = app
        
        self.pos = pos
        self.v = v
        self.r = r
        self.sprite = sprite
        self.start_condition = ['Entity', 'Died']
        self.new_condition = ['Entity', 'Died']

    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _move(self):
        pass

    def activity(self):
        pass

    def observe(self,other_entities):
        pass

    def _check_walls(self):
        pass
