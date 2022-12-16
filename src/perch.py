from abc import abstractmethod
import entity

class Perch(entity.Entity):
    @abstractmethod
    def __init__(self, app, pos, v, r, sprite):
        pass

    # @abstractmethod        
    # def __config_get(self, variable):
    #     pass

    @abstractmethod
    def _move(self):
        pass
    
    @abstractmethod
    def activity(self):
        pass

    @abstractmethod
    def observe(self):
        pass
    
    @abstractmethod
    def _check_walls(self, pos):
        pass
