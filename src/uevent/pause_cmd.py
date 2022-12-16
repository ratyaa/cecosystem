import uevent.command as command

class PauseCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Pauses the model."
        self.help_message = "\
------------------------\n\
Command: pause\n\
Description:\n\
\n\
Pauses the model. Use `resume` to resume it back.\n\
\n\
Options: nothing here yet :)\n\
        "

        self.app = app

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        self.app.paused = True
