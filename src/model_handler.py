import pygame
import entity
import perch_resting
import perch
import coord
from random import randint

class ModelHandler:
    def __init__(self, width, height, model_rate):
        self.width = width
        self.height = height
        self.model_rate = model_rate
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.entities = []
        self.__init_entities()

    def __init_entities(self):
        for i in range(15):
            self.entities.append(perch_resting.PerchResting(
                coord.Coord(randint(100, self.width - 100), randint(100, self.height - 100)),
                coord.Coord(float(randint(-2, 2)) / self.model_rate,
                      float(randint(-2, 2)) / self.model_rate),
                randint(10, 15),
                (255, 0, 0)
            ))
        
    def get_update_rate(self):
        return self.model_rate

    def draw(self):
        self.screen.fill((0, 0, 255))
        for entity in self.entities:
            pygame.draw.circle(
                self.screen,
                entity.sprite,
                (entity.pos.x, entity.pos.y),
                entity.r
            )
        pygame.display.update()

    def update(self):
        for entity in self.entities:
            entity.observe()
            entity.activity()

    