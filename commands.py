import os
import filecmp
from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def execute(self):
        pass

def create_command(command, *parameters):
    COMMAND_DICTIONARY = {
        "status": Status,
        "commit": Commit,
        "log": Log,
        "diff": Diff
    }

    if command in COMMAND_DICTIONARY:
        return COMMAND_DICTIONARY[command](*parameters)
    return f"{command} is not supported by git"


class Status(Command):
    def __init__(self, *parameters):
        self.path_specs = parameters[0]

    def check_is_list(self):
        if not isinstance(self.path_specs, list):
            raise TypeError("pathSpecs should be a list")

    def execute(self):
        return f"Status for: {', '.join(self.path_specs)}"

class Commit(Command):
    def __init__(self, *parameters):
        self.file_paths = parameters[0]
        self.message = parameters[1]

    def check_is_list(self):
        if not isinstance(self.file_paths, list):
            raise TypeError("filePaths should be a list")

    def execute(self):
        if not self.message:
            return "Please enter a commit message"
        for path in self.file_paths:
            if not os.path.exists(path):
                raise ValueError(f"{path} is not a valid file path")
        return f"Committed: {', '.join(self.file_paths)}"

class Log(Command):
    def __init__(self, *parameters):
        self.paths_to_show_log_for = parameters[0]

    def check_is_list(self):
        if not isinstance(self.paths_to_show_log_for, list):
            raise TypeError("pathsToShowLogFor should be a list")

    def execute(self):
        return f"Log for: {', '.join(self.paths_to_show_log_for)}"

class Diff(Command):
    def __init__(self, *paramaters):
        self.versions = paramaters[0]

        if len(self.versions) != 2:
            raise ValueError("diff command requires exactly 2 versions")
        self.file1 = self.versions[0]
        self.file2 = self.versions[1]

    def check_is_list(self):
        if not isinstance(self.versions, list):
            raise TypeError("versions should be a list")

    def execute(self):
        if not os.path.exists(self.file1):
            return "file is not a valid file path"
        if not os.path.exists(self.file2):
            return "file is not a valid file path"
        if filecmp.cmp(self.file1, self.file2):
            return "Files are identical"
        return "Files are different"
    