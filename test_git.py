import unittest
import os
from git import command_controller


def test_do_command_commit_invalid_file_path():
    filePaths = ["invalid_path1.txt", "invalid_path2.txt"]
    message = "test commit message"
    try:
        command_controller("commit", filePaths, message)
    except ValueError as e:
        assert str(e) == f"{filePaths[0]} is not a valid file path"
        assert os.path.exists(filePaths[0]) == False
        assert os.path.exists(filePaths[1]) == False


def test_do_command_commit_no_message():
    filePaths = ["test-files/test_file1.txt", "test-files/test_file2.txt"]
    message = ""
    result = command_controller("commit", filePaths, message)
    assert result == "Please enter a commit message"


def test_do_command_diff_invalid_file_path():
    versions = ["invalid_path1.txt", "invalid_path2.txt"]
    result = command_controller("diff", versions)
    assert result == "file is not a valid file path"


def test_do_command_diff_files_identical():
    versions = ["test_file1.txt", "test_file1_copy.txt"]
    result = command_controller("diff", versions)
    assert result == "Files are identical"


def test_do_command_diff_files_different():
    versions = ["test_file1.txt", "test_file2.txt"]
    result = command_controller("diff", versions)
    assert result == "Files are different"


if __name__ == "__main__":
    unittest.main()
