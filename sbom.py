import sys
from traverse import *

def main(argv):
    if (len(argv) != 2):
        print("Error, usage is: sbom.py [dir]")
        return 1
    
    directory = argv[1]
    print("Searching for repos in directory", directory)

    print("Found", findRepoTraverse(directory), "repos", "in", directory)

if __name__ == "__main__":
    main(sys.argv)