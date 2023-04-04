import sys
from traverse import *
from file_util import *

def main(argv):
    if (len(argv) != 2):
        print(f"Error, usage is: {argv[0]} [dir]")
        return 1
    
    directory = argv[1]
    print(f"Searching for repos in directory {directory}")

    clearOutput()

    repo_count = findRepoTraverse(directory)
    print(f"Found {repo_count} repos in {directory}")

if __name__ == "__main__":
    main(sys.argv)