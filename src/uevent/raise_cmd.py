import pygame
import uevent.command as command

class RaiseCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Opens the pygame window (raises hidden one)."
        self.help_message = "\
------------------------\n\
Command: raise\n\
Description:\n\
\n\
Open the pygame window if no one was opened.\n\
\n\
Options: nothing here yet :o\n\
        "
    
        self.app = app
        self.args = args

    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        if self.app.hidden:
            pygame.display.init()
            self.app.screen  = pygame.display.set_mode((
                self.__config_get('width'),
                self.__config_get('height'),
            ))
        self.app.hidden = False
