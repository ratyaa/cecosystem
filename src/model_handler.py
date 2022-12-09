import pygame
import entity
import perch_resting
import pike_resting
import perch_died
import perch
import coord
import app_config
from random import randint


class ModelHandler:
    def __init__(self, model_rate):
        self.width = app_config.WIDTH
        self.height = app_config.HEIGHT
        self.model_rate = model_rate
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.entities = []
        self.__init_entities()

    def __init_entities(self):
        for i in range(15):
            self.entities.append(perch_resting.PerchResting(
                coord.Coord(randint(100, self.width - 100), randint(100, self.height - 100)),
                coord.Coord(float(randint(-50, 50)),
                      float(randint(-50, 50))),
                randint(5, 10),
                (0, 255, 0)
            ))
        for i in range(1):
            self.entities.append(pike_resting.PikeResting(
                coord.Coord(randint(100, self.width - 100), randint(100, self.height - 100)),
                coord.Coord(float(randint(-50, 50)),  #
                            float(randint(-50, 50))),
                randint(15, 20),
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

    def entity_replace(self, number):
        if self.entities[number].new_condition != self.entities[number].start_condition:
            self.entities[number] = self.entities[number]._change_condition()

    def update(self):
        for i, entity in enumerate(self.entities):
            entity.observe(self.entities)
            self.entity_replace(i)
            entity.activity()

    
