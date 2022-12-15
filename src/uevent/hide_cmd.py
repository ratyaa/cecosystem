import pygame
import uevent.command as command

class HideCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Closes the pygame window (basically hides)."
        self.help_message = "\
------------------------\n\
Command: hide\n\
Description:\n\
\n\
Closes pygame window only (doesn't stop the model calculation, reversible via\n\
`raise`). Does nothing if there is already no pygame window.\n\
\n\
Options: nothing here yet :o\n\
        "

        self.app = app
        self.args = args

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        if not self.app.hidden:
            pygame.display.quit()
        self.app.hidden = True
