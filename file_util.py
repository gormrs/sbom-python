import os
import json


def writeCsv(name, version, packageManager, directory):
    # write data to csv file

    with open("sbom.csv", "a") as f:  
        f.write(f"{name},{version},{packageManager},{directory}\n")

    f.close()


def writeJson(name, version, packageManager, directory):
    # write data to json file

    data = {
        "name": name,
        "version": version,
        "packageManager": packageManager,
        "directory": directory
    }

    json_data = []
    
    # Read existing data from the file if it exists
    if os.path.exists("sbom.json"):
        try:
            with open("sbom.json", "r") as f:
                json_data = json.load(f)
        except IOError:
            print("Error reading sbom.json")
        except json.JSONDecodeError:
            print("Error decoding JSON data in sbom.json")

    # Append the new data
    json_data.append(data)

    # Write the updated data back to the file
    try:
        with open("sbom.json", "w") as f:
            json.dump(json_data, f, indent=2)
    except IOError:
        print("Error writing to sbom.json")
        

    f.close()

def clearOutput():
    if os.path.isfile("sbom.csv"):
        os.remove("sbom.csv")
    if os.path.isfile("sbom.json"):
        os.remove("sbom.json")
