import commands as cmd

def command_controller(command, *paramaters):
    """
    Takes in the user input and creates the object for checking for errors
    then executing the command.
    """
    inputCommand = cmd.create_command(command, *paramaters)
    inputCommand.check_is_list()
    return inputCommand.execute()