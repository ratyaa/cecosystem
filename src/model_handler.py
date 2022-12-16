import pygame
import entity
import perch_resting
import pike_resting
import perch_died
import perch
import coord
from random import randint


class ModelHandler:
    def __init__(self, app):
        self.app = app
        
        self.entities = []
        self.__init_entities()

    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def __init_entities(self):
        for i in range(45):
            self.entities.append(perch_resting.PerchResting(
                self.app,
                coord.Coord(
                    randint(100, self.__config_get('width') - 100),
                    randint(100, self.__config_get('height') - 100),
                ),
                coord.Coord(
                    float(randint(-50, 50)),
                    float(randint(-50, 50)),
                ),
                randint(5, 10),
                (0, 255, 0),
            ))
        for i in range(8):
            self.entities.append(pike_resting.PikeResting(
                self.app,
                coord.Coord(
                    randint(100, self.__config_get('width') - 100),
                    randint(100, self.__config_get('height') - 100)
                ),
                coord.Coord(
                    float(randint(-50, 50)),
                    float(randint(-50, 50))
                ),
                randint(15, 20),
                (255, 0, 0)
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

    def entity_replace(self, number):
        if self.entities[number].new_condition[1] == 'Division':
            self.entities.append(self.entities[number]._change_condition())
        if self.entities[number].new_condition != self.entities[number].start_condition:
            self.entities[number] = self.entities[number]._change_condition()

    def update(self):
        '''Вы можете быть озадачены наличием двух вызовов функции entity.observe...
        Это необходимо для исключения некоторых досаждающих багов.'''
        for i, entity in enumerate(self.entities):
            entity.observe(self.entities)
            entity.observe(self.entities)
            self.entity_replace(i)
            entity.activity()

    
