import pygame
import uevent.command as command

class HelpCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Your best friend in this exciting journey!"
        self.help_message = "\
------------------------\n\
Command: help\n\
Description:\n\
\n\
Prints help.\n\
\n\
Options:\n\
<cmd_name> <cmd_name> ...   	Prints help messages for all commands provided\n\
       				in the sequence of <cmd_name>'s. If there is no\n\
        			arguments, prints general help information\n\
        "
        
        self.app = app
        self.args = args

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        commands = self.__parse_args()
        
        if len(commands) == 0:
            self.__general_help()
            return
        
        self.__print_helps(set(commands))

    def __print_helps(self, commands):
        for command in commands:
            command = command(None, self.app)
            command._print_help()
        
    def __parse_args(self):
        commands = list(filter(
            lambda command: not command == None,
            map(self.app.event_handler.commands.get, self.args)
        ))
        
        return commands

    def __general_help(self):
        print("\
------------------------\n\
Cecosystem interactive console!\n\
\n\
Usage:\n\
<command> <arguments>\n\
\n\
IMPORTANT NOTE:\n\
Pressing the window's close button doesn't terminate the program, it just\n\
closes the pygame window (`hides` it, behaviour is the same as of the `hide`\n\
command). If you want to terminate the program, you need to invoke one of the\n\
termination commands listed below.\n\
\n\
Availabale commands:\n\
help <cmd_name>			Prints help message for the <cmd_name>.\n\
quit <args>        		Terminates program.\n\
exit <args>			Also terminates program (same behaviour).\n\
shutdown <args>       		Also terminates program (same behaviour!).\n\
hide				Closes pygame window only (doesn't stop the\n\
        			model calculation, reversible via `raise`).\n\
raise				Open pygame window (if closed).\n\
list				List all availible commands.\n\
...\n\
\n\
List more commands via `list` command.\n\
        ".expandtabs())
