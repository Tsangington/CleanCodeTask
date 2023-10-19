import commands as cmd

def command_controller(command, *paramaters):
    inputCommand = cmd.create_command(command, *paramaters)
    return inputCommand.execute()