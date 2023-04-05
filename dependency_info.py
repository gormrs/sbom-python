import sys
import os
import subprocess

def get_latest_commit(directory):
    if not directory:
        print("Error, no directory specified")
        sys.exit(1)
    
    if type(directory) != str:
        print("Error, directory must be a string")
        sys.exit(1)

    if not os.path.isdir(directory):
        print("Error, directory does not exist")
        sys.exit(1)

    try:
        output = subprocess.check_output(["git", "-C", directory, "log","--format=%H", "-n", "1"])
        decoded_output = output.decode("utf-8").strip()
        return decoded_output
    except subprocess.CalledProcessError:
        print("Error, git command failed")
        sys.exit(1)

def get_npm_link(name):
    if not name:
        print("Error, no name specified")
        sys.exit(1)
    
    if type(name) != str:
        print("Error, name must be a string")
        sys.exit(1)

    return f"https://www.npmjs.com/package/{name}"

def get_pypi_link(name):
    if not name:
        print("Error, no name specified")
        sys.exit(1)
    
    if type(name) != str:
        print("Error, name must be a string")
        sys.exit(1)

    return f"https://pypi.org/project/{name}"