import sys
from traverse import *
from file_util import *

def main(argv):
    if (len(argv) != 2):
        print(f"Error, usage is: {argv[0]} [dir]")
        return 
    
    directory = argv[1]
    print(f"Searching for repos in directory {directory}")

    clear_output()

    repo_count = find_repo_traverse(directory)
    print(f"Found {repo_count} repos in {directory}")
    print(f"Saved SBOM in CSV format to '{os.path.abspath('sbom.csv')}'")
    print(f"Saved SBOM in JSON format to '{os.path.abspath('sbom.json')}'")

if __name__ == "__main__":
    main(sys.argv)