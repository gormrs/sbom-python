import os

def findRepoTraverse(directory):
    repoCount = 0

    if not directory:
        print("Error, no directory specified")
        return 0
    
    if type(directory) != str:
        print("Error, directory must be a string")
        return 0 

    # checks if the directory is valid
    if not os.path.isdir(directory):
        print(f"Error, {directory} is not a valid directory")
        return 0
    
    


    for root, dirs, files in os.walk(directory):
        if ".git" in dirs:
            repoCount += 1
            
            dirs.remove(".git")


        for dir in dirs:
            findRepoTraverse(dir)

    return repoCount