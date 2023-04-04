import os

def findRepoTraverse(directory):
    repoCount = 0


    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            repoCount += 1
            
            dirs.remove(".git")


        for dir in dirs:
            findRepoTraverse(dir)

    return repoCount