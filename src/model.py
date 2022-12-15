import pygame
import model_handler
import asyncio

class Model():
    def __init__(self, app):
        self.app = app
        self.model_handler = model_handler.ModelHandler(self.app)
        self.draw_delay = 1.0 / self.app.config.framerate
        self.update_delay = 1.0 / self.app.config.update_rate

        pygame.init()
        pygame.display.update()
        
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
        
    async def __draw(self):
        while not self.app.finished:
            if not self.app.hidden:
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        await self.app.events.put("hide")
                        
                self.model_handler.draw()
                pygame.display.update
                
            await asyncio.sleep(self.draw_delay)
