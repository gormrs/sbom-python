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

    f.close()
            