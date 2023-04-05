import sys
import os
import subprocess


def get_latest_commit(directory):
    """
    Gets the latest commit hash for the git repository located in the specified directory.

    :param directory: The directory containing the git repository
    :return: The latest commit hash as a string
    """
    if not directory:
        print("Error, no directory specified")
        sys.exit(1)

    if not isinstance(directory, str):
        print("Error, directory must be a string")
        sys.exit(1)

    if not os.path.isdir(directory):
        print("Error, directory does not exist")
        sys.exit(1)

    try:
        output = subprocess.check_output(
            ["git", "-C", directory, "log", "--format=%H", "-n", "1"])
        decoded_output = output.decode("utf-8").strip()
        return decoded_output
    except subprocess.CalledProcessError:
        print("Error, git command failed")
        sys.exit(1)


def get_npm_link(name):
    """
    Generates the npm package URL for the given package name.

    :param name: The name of the npm package
    :return: The URL of the npm package page as a string
    """
    if not name:
        print("Error, no name specified")
        sys.exit(1)

    if not isinstance(name, str):
        print("Error, name must be a string")
        sys.exit(1)

    return f"https://www.npmjs.com/package/{name}"


def get_pypi_link(name):
    """
    Generates the PyPI package URL for the given package name.

    :param name: The name of the PyPI package
    :return: The URL of the PyPI package page as a string
    """
    if not name:
        print("Error, no name specified")
        sys.exit(1)

    if not isinstance(name, str):
        print("Error, name must be a string")
        sys.exit(1)

    return f"https://pypi.org/project/{name}"
