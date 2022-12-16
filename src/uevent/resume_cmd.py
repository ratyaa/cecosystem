import uevent.command as command

class ResumeCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Resumes the model."
        self.help_message = "\
------------------------\n\
Command: resume\n\
Description:\n\
\n\
Resumes the model. Use `pause` to pause it back.\n\
\n\
Options: nothing here yet :)\n\
        "

        self.app = app

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        self.app.paused = False
