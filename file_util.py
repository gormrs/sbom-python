import os
import json


def write_csv(name, version, packageManager, directory, commit, link):
    # write data to csv file

    with open("sbom.csv", "a", encoding='utf-8') as sbom_csv:
        sbom_csv.write(
            f"{name},{version},{packageManager},{directory},{commit},{link}\n")

    sbom_csv.close()


def write_json(name, version, packageManager, directory, commit, link):
    # write data to json file

    data = {
        "name": name,
        "version": version,
        "packageManager": packageManager,
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
    if os.path.isfile("sbom.csv"):
        os.remove("sbom.csv")
    if os.path.isfile("sbom.json"):
        os.remove("sbom.json")
