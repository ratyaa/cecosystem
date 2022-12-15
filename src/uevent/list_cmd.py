import uevent.command as command

class ListCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Prints all available commands."
        self.help_message = "\
------------------------\n\
Command: list\n\
Description:\n\
\n\
Prints all available commands with short descriptions.\n\
\n\
Options: nothing here yet :o\n\
        "
        
        self.app = app

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        print("\
------------------------\n\
Available commands:\n\
        ")
        commands = self.app.event_handler.commands.items()
        for key, value in commands:
            row = (key + "\t\t\t\t\t".expandtabs())[:32]
            row = row + value(None, None).short_help_message
            print(row)
        print()
            
