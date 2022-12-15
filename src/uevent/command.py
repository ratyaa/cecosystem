from abc import abstractmethod, ABC

class Command(ABC):
    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def _print_help(self):
        pass
