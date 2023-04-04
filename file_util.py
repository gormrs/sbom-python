import os


def writeCsv(name, version, packageManager, directory):
    # write data to csv file

    with open("sbom.csv", "a") as f:  
        f.write(f"{name},{version},{packageManager},{directory}\n")

    f.close()

def clearOutput():
    if os.path.isfile("sbom.csv"):
        os.remove("sbom.csv")
