import pygame
import asyncio

import config
import model
import ui
import uevent.event_handler as event_handler

class App:
    def __init__(self, config_file="config.yaml", defaults_file='src/.config_defaults.yaml'):
        self.config = config.AppConfig(config_file, defaults_file)
        
        self.finished = False
        self.hidden = False
        self.paused = False

        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((
            self.__config_get('width'),
            self.__config_get('height'),
        ))

    def __config_get(self, variable):
        return self.config.app_vars.get(variable).get_value()

    async def run(self):
        self.events = asyncio.Queue()
        await self.events.put('help')
        
        self.model = model.Model(self)
        self.event_handler = event_handler.EventHandler(self)
        self.user_input_handler = ui.UserInputHandler(self)

        tasks = (
            self.model.run(),
            self.user_input_handler.run(),
            self.event_handler.run(),
        )
        self.task_group = asyncio.gather(*tasks)

        await self.task_group
        await self.events.join()        
        
