import pygame
import model_handler
import asyncio

class Model():
    def __init__(self, app):
        self.app = app
        
        self.model_handler = model_handler.ModelHandler(self.app)
        self.draw_delay = 1.0 / self.__config_get('framerate')
        self.update_delay = 1.0 / self.__config_get('update_rate')

        pygame.init()
        pygame.display.update()
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()
    
    async def run(self):
        tasks = (
            self.__update(),
            self.__draw(),
        )
        await asyncio.gather(*tasks)

    async def __update(self):
        while not self.app.finished:
            self.model_handler.update()

            await asyncio.sleep(self.update_delay)
            await self.__pause()
        
    async def __draw(self):
        while not self.app.finished:
            if not self.app.hidden:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        await self.app.events.put("hide")
                        
                self.model_handler.draw()
                pygame.display.update

            await asyncio.sleep(self.draw_delay)
            await self.__pause()

    async def __pause(self):
        while self.app.paused:
            await asyncio.sleep(0.5)
