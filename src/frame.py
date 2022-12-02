from abc import ABC, abstractmethod

class Frame(ABC):
    @abstractmethod
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def update(self):
        pass
