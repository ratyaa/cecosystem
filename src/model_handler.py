import pygame
import entity
import perch_resting
import perch
import coord
from random import randint

class ModelHandler:
    def __init__(self, app):
        self.app = app
        self.entities = []
        self.__init_entities()

    def __init_entities(self):
        for i in range(15):
            self.entities.append(perch_resting.PerchResting(
                coord.Coord(
                    randint(100, self.app.config.width - 100),
                    randint(100, self.app.config.height - 100)
                ),
                coord.Coord(float(randint(-50, 50)), # 
                      float(randint(-50, 50))),
                randint(10, 15),
                (255, 0, 0),
                self.app
            ))
        
    def draw(self):
        self.app.screen.fill((0, 0, 255))
        for entity in self.entities:
            pygame.draw.circle(
                self.app.screen,
                entity.sprite,
                (entity.pos.x, entity.pos.y),
                entity.r
            )
        pygame.display.update()

    def update(self):
        for entity in self.entities:
            entity.observe()
            entity.activity()

    
