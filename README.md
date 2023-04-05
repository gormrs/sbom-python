## Python SBOM Generator
This SBOM Generator is a Python script that helps you generate a Software Bill of Materials (SBOM) for your repositories. It supports Python and JavaScript projects with **requirements.txt** and **package.json** files, respectively.

The generated SBOM will be output in both CSV and JSON formats, containing information about each dependency, including its name, version, package manager, repository directory, commit hash, and package URL.

## Features
* Supports Python (using requirements.txt) and JavaScript (using package.json) projects
* Generates SBOM in CSV and JSON formats
* Traverses through specified directory to find repositories
* Extracts dependency information, including commit hash and package URL

## Usage
1. Clone the repository or download the source code.

2. Make sure you have Python installed on your system.

3. Navigate to the directory containing the script using the command line or terminal.

4. Run the script with the following command:

`python sbom.py [directory]`

Replace [directory] with the path to the directory containing your repositories.

5. The script will traverse the specified directory and generate an SBOM for each detected repository with a requirements.txt or package.json file.

6. The generated SBOM files, sbom.csv and sbom.json, will be saved in the same directory as the script.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Features to implement

* Add info about what the latest version of the dependency is
* Info about the last time the dependency was updated
* Info about the license of the dependency
* Any know vulnerabilities in the dependency and the severity of the vulnerability (if possible)
* Licensing inforamtion to know if you can use the dependency
* Description of the dependency
