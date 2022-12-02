from abc import abstractmethod
import entity

class Perch(entity.Entity):
    @abstractmethod
    def __init__(self, pos, v, r, sprite):
        pass

    @abstractmethod
    def _move(self):
        pass

    @abstractmethod
    def activity(self):
        pass

    @abstractmethod
    def observe(self):
        pass
        
