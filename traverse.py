import json
import os
import sys
from file_util import write_csv, write_json
from dependency_info import get_latest_commit, get_npm_link, get_pypi_link


def find_repo_traverse(directory):
    """
    Traverse the given directory to find repositories and generate an SBOM
    for each repository with a requirements.txt or package.json file.

    Args:
        directory (str): The path to the directory to search for repositories.

    Returns:
        int: The number of repositories found in the directory.
    """
    repo_count = 0
    found_a_sbomfile = False

    if not directory:
        print("Error, no directory specified")
        sys.exit(1)

    if isinstance(directory) != str:
        print("Error, directory must be a string")
        sys.exit(1)

    if not os.path.isdir(directory):
        print("Error, directory does not exist")
        sys.exit(1)

    for root, dirs in os.walk(directory):
        if ".git" in dirs:
            repo_count += 1
            if "requirements.txt" in os.listdir(root):
                get_python_requirements(root)
                found_a_sbomfile = True
            if "package.json" in os.listdir(root):
                get_js_dependencies(root)
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
    """
    Process the requirements.txt file in the given directory and extract
    the Python dependencies to generate an SBOM.

    Args:
        directory (str): The path to the repository directory containing the
                         requirements.txt file.
    """
    if "requirements.txt" not in os.listdir(directory):
        return

    with open(os.path.join(directory, "requirements.txt"), "r", encoding='utf-8') as pip_file:
        for line in pip_file:
            row = line.split("==")
            if len(row) == 2:
                name = row[0].strip()
                version = row[1].strip()
                commit = get_latest_commit(directory)
                link = get_pypi_link(name)

                write_csv(name, version, "pip", directory, commit, link)
                write_json(name, version, "pip", directory, commit, link)

    pip_file.close()


def get_js_dependencies(directory):
    """
    Process the package.json file in the given directory and extract
    the JavaScript dependencies to generate an SBOM.

    Args:
        directory (str): The path to the repository directory containing the
                         package.json file.
    """
    if "package.json" not in os.listdir(directory):
        return

    with open(os.path.join(directory, "package.json"), "r", encoding='utf-8') as npm_file:
        data = json.load(npm_file)
        for dependency in data["dependencies"]:
            name = dependency
            version = data["dependencies"][dependency]
            commit = get_latest_commit(directory)
            link = get_npm_link(name)

            write_csv(name, version, "npm", directory, commit, link)
            write_json(name, version, "npm", directory, commit, link)

    npm_file.close()
