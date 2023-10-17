import os
import filecmp
import command as cmd

def command_controller(command, *paramaters):
    inputCommand = cmd.CommandFactory().create_command(command, *paramaters)
    return inputCommand.execute()