from abc import ABC, abstractmethod

class Pike(ABC):
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