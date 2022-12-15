import asyncio
import events

class EventHandler:
    def __init__(self, app):
        self.app = app
        self.events = {
            'stop': events.ShutdownEvent,
            'hide': events.HideEvent,
            'raise': events.RaiseEvent,
            'help': events.HelpEvent,
        }

    async def run(self):
        while not self.app.finished:
            event = self.events.get(await self.app.events.get())
            if not event == None:
                event.handle(self.app)

            self.app.events.task_done()
            await asyncio.sleep(0.1)




