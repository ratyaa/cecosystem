import asyncio

import uevent.shutdown_cmd as shutdown_cmd
import uevent.help_cmd as help_cmd
import uevent.hide_cmd as hide_cmd
import uevent.raise_cmd as raise_cmd
import uevent.list_cmd as list_cmd
import uevent.pause_cmd as pause_cmd
import uevent.resume_cmd as resume_cmd
import uevent.var_cmd as var_cmd

class EventHandler:
    def __init__(self, app):
        self.app = app
        self.commands = {
            'exit': 		shutdown_cmd.ShutdownCommand,
            'shutdown': 	shutdown_cmd.ShutdownCommand,
            'quit': 		shutdown_cmd.ShutdownCommand,
            'hide': 		hide_cmd.HideCommand,
            'raise': 		raise_cmd.RaiseCommand,
            'help': 		help_cmd.HelpCommand,
            'list':		list_cmd.ListCommand,
            'pause':		pause_cmd.PauseCommand,
            'resume':		resume_cmd.ResumeCommand,
            'var':		var_cmd.VarCommand,
        }

    async def run(self):
        while not self.app.finished: 
            user_input = list(map(str, (await self.app.events.get()).split()))

            try:
                command = user_input[0]
            except:
                continue
            args = user_input[1:]
            
            event = self.commands.get(command, list_cmd.ListCommand)
            event(args, self.app).handle()
            
            self.app.events.task_done()
            await asyncio.sleep(0.1)
