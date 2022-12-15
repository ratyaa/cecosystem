from abc import abstractmethod, ABC
import pygame

class Event(ABC):
    @staticmethod
    def handle(app):
        pass

class ShutdownEvent(Event):
    @staticmethod
    def handle(app):
        app.finished = True

class HideEvent(Event):
    @staticmethod
    def handle(app):
        if not app.hidden:
            pygame.display.quit()
        app.hidden = True

class RaiseEvent(Event):
    @staticmethod
    def handle(app):
        if app.hidden:
            pygame.display.init()
            app.screen  = pygame.display.set_mode((app.config.width, app.config.height))
        app.hidden = False

class HelpEvent(Event):
    @staticmethod
    def handle(app):
        print("Help!")
