import asyncio
import threading

class UserInputHandler:
    def __init__(self, app):
        self.app = app

    async def run(self):
        while not self.app.finished:
            await self.app.events.put(await self.__ainput())
            await asyncio.sleep(0.1)

    async def __ainput(self):
        loop = asyncio.get_event_loop()
        handle_user_input = loop.create_future()
        
        def _run():
            user_input = input(" -> ")
            loop.call_soon_threadsafe(handle_user_input.set_result, user_input)

        threading.Thread(target=_run, daemon=True).start()
        return await handle_user_input

        
