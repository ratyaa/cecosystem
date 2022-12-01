from abc import ABC, abstractmethod
import Frame

class Perch(ABC, Frame):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __move(self):
        pass

    @abstractmethod
    def activity(self):
        pass

    @abstractmethod
    def observe(self, entities):
        pass
        
