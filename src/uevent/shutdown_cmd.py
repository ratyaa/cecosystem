import pygame
import uevent.command as command

class ShutdownCommand(command.Command):

    def __init__(self, args, app):
        self.short_help_message = "Terminates program."
        self.help_message = "\
------------------------\n\
Commands: shutdown, exit, quit (same behavior)\n\
Description:\n\
\n\
Terminates program.\n\
\n\
Options: nothing here yet :o\n\
        "
# --save-config, -c		Save current configuration into the config file.\n\
        

        self.app = app
        self.args = args

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        self.app.finished = True
