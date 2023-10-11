import os
import filecmp


def do_command(command, pathSpecs, filePaths, pathsToShowLogFor, versions, message):
    """
    Executes the specified Git command with the given arguments.

    Args:
        command (str): The Git command to execute.
        pathSpecs (list): A list of file path patterns to include in the command.
        filePaths (list): A list of file paths to include in the command.
        pathsToShowLogFor (list): A list of file paths to show logs for.
        versions (list): A list of versions to compare for the "diff" command.
        message (str): The commit message to use for the "commit" command.

    Returns:
        str: The result of the Git command.

    Raises:
        TypeError: If any of the input arguments are not lists.
        ValueError: If the "diff" command is used with a number of versions other than 2,
                    or if any of the specified file paths do not exist for the "commit" command.
    """
    if not isinstance(pathSpecs, list):
        raise TypeError("pathSpecs should be a list")
    if not isinstance(filePaths, list):
        raise TypeError("filePaths should be a list")
    if not isinstance(pathsToShowLogFor, list):
        raise TypeError("pathsToShowLogFor should be a list")
    if not isinstance(versions, list):
        raise TypeError("versions should be a list")

    if command == "status":
        return status(pathSpecs)
    elif command == "commit":
        return commit(filePaths, message)
    elif command == "log":
        return log(pathsToShowLogFor)
    elif command == "diff":
        if len(versions) != 2:
            raise ValueError("diff command requires exactly 2 versions")
        return diff(versions[0], versions[1])
    else:
        return f"{command} is not supported by git"


def status(pathSpecs):
    return f"Status for: {', '.join(pathSpecs)}"


def commit(filePaths, message):
    if not message:
        return "Please enter a commit message"
    for path in filePaths:
        if not os.path.exists(path):
            raise ValueError(f"{path} is not a valid file path")
    return f"Committed: {', '.join(filePaths)}"


def log(pathsToShowLogFor):
    return f"Log for: {', '.join(pathsToShowLogFor)}"


def diff(file1, file2):
    if not os.path.exists(file1):
        return "file is not a valid file path"
    if not os.path.exists(file2):
        return "file is not a valid file path"
    # Compare two files using filecmp
    if filecmp.cmp(file1, file2):
        return "Files are identical"
    else:
        return "Files are different"
