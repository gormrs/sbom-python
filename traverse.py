import json
import os
from file_util import *

def find_repo_traverse(directory):
    repo_count = 0

    if not directory:
        print("Error, no directory specified")
        return 0
    
    if type(directory) != str:
        print("Error, directory must be a string")
        return 0 

    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            repo_count += 1
            if "requirements.txt" in os.listdir(root):
                get_python_requirements(root)
            if "package.json" in os.listdir(root):
                get_java_dependencies(root)
            dirs.remove(".git")


    return repo_count

def get_python_requirements(directory):
    if "requirements.txt" not in os.listdir(directory):
        return
    
    with open(os.path.join(directory, "requirements.txt"), "r") as f:
        for line in f:
            row = line.split("==")
            if len(row) == 2:
                name = row[0].strip()
                version = row[1].strip()
                write_csv(name, version, "pip", directory)
                write_json(name, version, "pip", directory)

    f.close()

def get_java_dependencies(directory):
    if "package.json" not in os.listdir(directory):
        return
    
    # todo: add a flag for dev dependencies
    with open(os.path.join(directory, "package.json"), "r") as f:
        data = json.load(f)
        for dependency in data["dependencies"]:
            name = dependency
            version = data["dependencies"][dependency]
            write_csv(name, version, "npm", directory)
            write_json(name, version, "npm", directory)