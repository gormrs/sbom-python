import sys
import os
from traverse import find_repo_traverse
from file_util import clear_output


def main(argv):
    """
    Entry point for the SBOM Generator script. This function processes the
    command-line arguments, clears the previous output files, and generates
    the SBOM for the given directory.

    Args:
        argv (list): A list containing the command-line arguments, where
                     argv[1] is expected to be the directory to search for
                     repositories.

    Exits:
        2: If an incorrect number of arguments are provided.
    """
    if len(argv) != 2:
        print(f"Error, usage is: {argv[0]} [dir]")
        sys.exit(2)
    directory = argv[1]
    print(f"Searching for repos in directory {directory}")

    clear_output()

    repo_count = find_repo_traverse(directory)
    print(f"Found {repo_count} repos in {directory}")
    print(f"Saved SBOM in CSV format to '{os.path.abspath('sbom.csv')}'")
    print(f"Saved SBOM in JSON format to '{os.path.abspath('sbom.json')}'")


if __name__ == "__main__":
    main(sys.argv)
