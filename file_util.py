import os
import json


def write_csv(name, version, package_manager, directory, commit, link):
    """
    Writes dependency information to the sbom.csv file.

    :param name: The name of the dependency
    :param version: The version of the dependency
    :param package_manager: The package manager used for the dependency (e.g. 'pip' or 'npm')
    :param directory: The directory of the project containing the dependency
    :param commit: The commit hash of the project
    :param link: The URL of the dependency's package page
    """
    # write data to csv file

    with open("sbom.csv", "a", encoding='utf-8') as sbom_csv:
        sbom_csv.write(
            f"{name},{version},{package_manager},{directory},{commit},{link}\n")

    sbom_csv.close()


def write_json(name, version, package_manager, directory, commit, link):
    """
    Writes dependency information to the sbom.json file.

    :param name: The name of the dependency
    :param version: The version of the dependency
    :param package_manager: The package manager used for the dependency (e.g. 'pip' or 'npm')
    :param directory: The directory of the project containing the dependency
    :param commit: The commit hash of the project
    :param link: The URL of the dependency's package page
    """

    data = {
        "name": name,
        "version": version,
        "package_manager": package_manager,
        "directory": directory,
        "commit": commit,
        "link": link,       # traling comma
    }

    json_data = []

    # Read existing data from the file if it exists
    if os.path.exists("sbom.json"):
        try:
            with open("sbom.json", "r", encoding='utf-8') as sbom_csv:
                json_data = json.load(sbom_csv)
        except IOError:
            print("Error reading sbom.json")
        except json.JSONDecodeError:
            print("Error decoding JSON data in sbom.json")

    # Append the new data
    json_data.append(data)

    # Write the updated data back to the file
    try:
        with open("sbom.json", "w", encoding='utf-8') as sbom_csv:
            json.dump(json_data, sbom_csv, indent=2)
    except IOError:
        print("Error writing to sbom.json")

    sbom_csv.close()


def clear_output():
    """
    Removes sbom.csv and sbom.json files if they exist in the current working directory.
    """
    if os.path.isfile("sbom.csv"):
        os.remove("sbom.csv")
    if os.path.isfile("sbom.json"):
        os.remove("sbom.json")
