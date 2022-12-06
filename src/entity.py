from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _move(self):
        pass

    @abstractmethod
    def observe(self):
        pass

    @abstractmethod
    def activity(self):
        pass
    
    @abstractmethod
    def _check_walls(self):
        pass    
