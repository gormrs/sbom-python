import json
import os
from file_util import *

def findRepoTraverse(directory):
    repoCount = 0

    if not directory:
        print("Error, no directory specified")
        return 0
    
    if type(directory) != str:
        print("Error, directory must be a string")
        return 0 

    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            repoCount += 1
            if "requirements.txt" in os.listdir(root):
                getPythonRequirements(root)
            if "package.json" in os.listdir(root):
                getJavaDependencies(root)
            dirs.remove(".git")


    return repoCount

def getPythonRequirements(directory):
    if "requirements.txt" not in os.listdir(directory):
        return
    
    with open(os.path.join(directory, "requirements.txt"), "r") as f:
        for line in f:
            row = line.split("==")
            if len(row) == 2:
                name = row[0].strip()
                version = row[1].strip()
                writeCsv(name, version, "pip", directory)
                writeJson(name, version, "pip", directory)

    f.close()

def getJavaDependencies(directory):
    if "package.json" not in os.listdir(directory):
        return
    
    # todo: add a flag for dev dependencies
    with open(os.path.join(directory, "package.json"), "r") as f:
        data = json.load(f)
        for dependency in data["dependencies"]:
            name = dependency
            version = data["dependencies"][dependency]
            writeCsv(name, version, "npm", directory)
            writeJson(name, version, "npm", directory)