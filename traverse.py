import json
import os
from file_util import *
import sys
from dependency_info import *

def find_repo_traverse(directory):
    repo_count = 0
    found_a_sbomfile = False

    if not directory:
        print("Error, no directory specified")
        sys.exit(1)
    
    if type(directory) != str:
        print("Error, directory must be a string")
        sys.exit(1)

    if not os.path.isdir(directory):
        print("Error, directory does not exist")
        sys.exit(1)

    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            repo_count += 1
            if "requirements.txt" in os.listdir(root):
                get_python_requirements(root)
                found_a_sbomfile = True
            if "package.json" in os.listdir(root):
                get_java_dependencies(root)
                found_a_sbomfile = True
            dirs.remove(".git")

    if repo_count == 0:
        print("Error, no repos found")
        sys.exit(1)

    if not found_a_sbomfile:
        print("Error, no sbom file found")
        sys.exit(1)
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
                commit = get_latest_commit(directory)
                link = get_pypi_link(name)

                write_csv(name, version, "pip", directory, commit, link)
                write_json(name, version, "pip", directory, commit, link)

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
            commit = get_latest_commit(directory)
            link = get_npm_link(name)

            write_csv(name, version, "npm", directory, commit, link)
            write_json(name, version, "npm", directory, commit, link)