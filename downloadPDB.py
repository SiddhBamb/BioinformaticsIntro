import os
import argparse
import requests

# make PDB directory if it doesn't already exist
if not os.path.isdir("PDB"):
    os.mkdir("PDB")

# read in command line argument for the python program: the only input is the txt file with a list of PDB IDs
parser = argparse.ArgumentParser(description="download PDBs for each protein in the input text file")
parser.add_argument('file', type=argparse.FileType('r'), help="input file of PDB IDs")
args = parser.parse_args()

with args.file as file:
    proteins = file.read().split()

    # add file extension to every element of the list of PDB IDs
    proteins = [(p + ".cif") for p in proteins]
    for protein in proteins:
        # if the file has already been downloaded, skip to save time (for runs after the first time)
        if os.path.isfile(os.path.join("PDB",protein)):
            continue
        # load the file from the following URL into a variable
        r = requests.get('http://files.rcsb.org/download/'+protein)
        # write the newly created variable into a new file with the same name as the file requested, in the PDB directory
        open(os.path.join("PDB",protein), "wb").write(r.content)
