import uevent.command as command
from collections import deque

class VarCommand(command.Command):
    def __init__(self, args, app):
        self.short_help_message = "Configurate the model."
        self.help_message = "\
------------------------\n\
Command: var\n\
Description:\n\
\n\
Modifies model parameters.\n\
\n\
Usage:\n\
var <var_name> <operation> <value>\n\
        "

        self.app = app
        self.args = args

        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            'set': lambda x, y: x,
        }
        
    def __config_get(self, variable):
        return self.app.config.app_vars.get(variable).get_value()

    def _print_help(self):
        print(self.help_message)

    def handle(self):
        args = deque(self.args)
        try:
            variable = self.app.config.app_vars.get(args.popleft())
            operation = self.operations.get(args.popleft())
            operation_value = float(args.popleft())
        except:
            print("Oops! Something went wrong :(")
            self._print_help()
            return

        variable.set_value(
            operation(operation_value, variable.get_value())
        )
