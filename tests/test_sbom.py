import os
import subprocess
import sys
import json
import tempfile
import shutil
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from traverse import find_repo_traverse, get_python_requirements, get_js_dependencies
from file_util import clear_output, write_csv, write_json
from dependency_info import get_latest_commit, get_npm_link, get_pypi_link

class TestSbom(unittest.TestCase):

    def test_write_json(self):
        write_json("test_dependency", "1.0.0", "npm", "/path/to/repo", "1234567890abcdef", "https://www.npmjs.com/package/test_dependency")
        
        with open("sbom.json", "r", encoding='utf-8') as sbom_json:
            data = json.load(sbom_json)
            
        os.remove("sbom.json")

        
        assert data[0]["name"] == "test_dependency"
        assert data[0]["version"] == "1.0.0"
        assert data[0]["package_manager"] == "npm"
        assert data[0]["directory"] == "/path/to/repo"
        assert data[0]["commit"] == "1234567890abcdef"
        assert data[0]["link"] == "https://www.npmjs.com/package/test_dependency"


    def test_write_csv(self):
        write_csv("test_dependency", "1.0.0", "npm", "/path/to/repo", "1234567890abcdef", "https://www.npmjs.com/package/test_dependency")
        
        with open("sbom.csv", "r", encoding='utf-8') as sbom_csv:
            data = sbom_csv.read()
            
        os.remove("sbom.csv")
        
        assert data == "test_dependency,1.0.0,npm,/path/to/repo,1234567890abcdef,https://www.npmjs.com/package/test_dependency\n"

    def test_clear_output(self):
        write_csv("test_dependency", "1.0.0", "npm", "/path/to/repo", "1234567890abcdef", "https://www.npmjs.com/package/test_dependency")
        write_json("test_dependency", "1.0.0", "npm", "/path/to/repo", "1234567890abcdef", "https://www.npmjs.com/package/test_dependency")
        
        clear_output()
        
        assert not os.path.exists("sbom.csv")
        assert not os.path.exists("sbom.json")

    def test_get_npm_link(self):
        assert get_npm_link("test_dependency") == "https://www.npmjs.com/package/test_dependency"

    def test_get_pypi_link(self):
        assert get_pypi_link("test_dependency") == "https://pypi.org/project/test_dependency"

    def create_temp_git_repo(self):
        temp_dir = tempfile.mkdtemp()
        subprocess.run(["git", "init"], cwd=temp_dir)

        with open(os.path.join(temp_dir, "temp_file.txt"), "w") as temp_file:
            temp_file.write("Temporary content")

        with open(os.path.join(temp_dir, "requirements.txt"), "w") as f:
                f.write("test_package==1.0.0\n")

            # Create a fake repository with a package.json file
        with open(os.path.join(temp_dir, "package.json"), "w") as f:
            json.dump({"dependencies": {"test_package": "1.0.0"}}, f)

        subprocess.run(["git", "add", "temp_file.txt"], cwd=temp_dir)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=temp_dir)
        

        return temp_dir

    def test_get_latest_commit(self):
        test_sbom = TestSbom()
        temp_repo_path = test_sbom.create_temp_git_repo()
        commit_hash = subprocess.check_output(["git", "log", "--format=%H", "-n", "1"], cwd=temp_repo_path).decode("utf-8").strip()
        
        assert get_latest_commit(temp_repo_path) == commit_hash

        # Clean up the temporary directory
        shutil.rmtree(temp_repo_path)

    def test_find_repo_traverse(self):
        test_sbom = TestSbom()
        temp_dir = test_sbom.create_temp_git_repo()

        try:
            
            repo_count = find_repo_traverse(temp_dir)
            assert repo_count == 1
        finally:
            shutil.rmtree(temp_dir)


    def test_get_python_requirements(self):
        test_sbom = TestSbom()
        temp_dir = test_sbom.create_temp_git_repo()

        try:
            get_python_requirements(temp_dir)
            assert os.path.isfile("sbom.csv")
            assert os.path.isfile("sbom.json")
        finally:
            shutil.rmtree(temp_dir)
            os.remove("sbom.csv")
            os.remove("sbom.json")


    def test_get_js_dependencies(self):
        test_sbom = TestSbom()
        temp_dir = test_sbom.create_temp_git_repo()

        try:
            get_js_dependencies(temp_dir)
            assert os.path.isfile("sbom.csv")
            assert os.path.isfile("sbom.json")
        finally:
            shutil.rmtree(temp_dir)
            os.remove("sbom.csv")
            os.remove("sbom.json")


def run_tests():
    test_sbom = TestSbom()
    print("Running tests test_write_json()...")
    test_sbom.test_write_json()
    print("Running tests test_write_csv()...")
    test_sbom.test_write_csv()
    print("Running tests test_clear_output()...")
    test_sbom.test_clear_output()
    print("Running tests test_get_npm_link()...")
    test_sbom.test_get_npm_link()
    print("Running tests test_get_pypi_link()...")
    test_sbom.test_get_pypi_link()
    print("Running tests test_get_latest_commit()...")
    test_sbom.test_get_latest_commit()
    print("Running tests test_find_repo_traverse()...")
    test_sbom.test_find_repo_traverse()
    print("Running tests test_get_python_requirements()...")
    test_sbom.test_get_python_requirements()
    print("Running tests test_get_js_dependencies()...")
    test_sbom.test_get_js_dependencies()
    print("All tests passed!")


if __name__ == "__main__":
    unittest.main()