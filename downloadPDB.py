import os
import argparse
import requests

if not os.path.isdir("PDB"):
    os.mkdir("PDB")

parser = argparse.ArgumentParser(description="download PDBs for each protein in the input text file")
parser.add_argument('file', type=argparse.FileType('r'), help="input file of PDB IDs")
args = parser.parse_args()

with args.file as file:
    proteins = file.read().split()
    proteins = [(p + ".cif") for p in proteins]
    for protein in proteins:
        if os.path.isfile(os.path.join("PDB",protein)):
            continue
        r = requests.get('http://files.rcsb.org/download/'+protein)
        open(os.path.join("PDB",protein), "wb").write(r.content)

