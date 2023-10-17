import os
import filecmp

class CommandFactory:
    def __init__(self):
        pass

    def create_command(self, command, *parameters):
        self.command = command
        COMMANDDICTIONARY = {
            "status": Status,
            "commit": Commit,
            "log": Log,
            "diff": Diff
        }
        print(f"Command is: {self.command}")
        if command in COMMANDDICTIONARY:
            return COMMANDDICTIONARY[self.command](*parameters)
        else:
            return f"{command} is not supported by git"

class Command:
    def __init__(self) -> None:
        pass

class Status(Command):
    def __init__(self, *parameters):
        self.pathSpecs = parameters[0]
    
    def execute(self):
        return f"Status for: {', '.join(self.pathSpecs)}"
    
class Commit(Command):
    def __init__(self, *parameters):
        print(parameters[0])
        self.filePaths = parameters[0]
        self.message = parameters[1]
    
    def execute(self):
        if not self.message:
            return "Please enter a commit message"
        for path in self.filePaths:
            if not os.path.exists(path):
                raise ValueError(f"{path} is not a valid file path")
        return f"Committed: {', '.join(self.filePaths)}"


class Log(Command):
    def __init__(self, *parameters):
        self.pathsToShowLogFor = parameters[0]

    def execute(self):
        return f"Log for: {', '.join(self.pathsToShowLogFor)}"

class Diff(Command):
    def __init__(self, *paramaters):
        self.versions = paramaters[0]
        print(self.versions)
        if len(self.versions) != 2:
            raise ValueError("diff command requires exactly 2 versions") 
        self.file1 = self.versions[0]
        self.file2 = self.versions[1]

    def execute(self):
        if not os.path.exists(self.file1):
            return "file is not a valid file path"
        if not os.path.exists(self.file2):
            return "file is not a valid file path"
        if filecmp.cmp(self.file1, self.file2):
            return "Files are identical"
        else:
            return "Files are different"

