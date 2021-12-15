import os
import argparse
import gemmi
from gemmi import cif
from collections import Counter

# make PDB directory so this program gives a meaningful error message if the file doesn't exist
if not os.path.isdir("PDB"):
    os.mkdir("PDB")

# read in the name of the CIF file to be read for frequencies
parser = argparse.ArgumentParser(description="count amino acids in all unique chains")
parser.add_argument('file', help="input CIF file")
args = parser.parse_args()

# parse the file as a CIF and for its structures
protein = cif.read_file(os.path.join("PDB",args.file))
model = gemmi.read_structure(os.path.join("PDB",args.file))
unique_chains = {}
# go through each chain in each model and keep only non duplicate ones
for modelNum in range(len(model)):
    for chainNum in range(len(model[modelNum])):
        # using a dictionary with key = string representing the chain and value = gemmi.Chain object
        # print("".join([str(model[modelNum][chainNum][i]) for i in range(len(model[modelNum][chainNum]))]))
        unique_chains[", ".join([str(model[modelNum][chainNum][i]) for i in range(len(model[modelNum][chainNum]))])] = model[modelNum][chainNum]
# print(unique_chains)

# use Counter to find residue frequencies after flattening all unique chains into one list of all residues
# residues_all = []
# for c in unique_chains.keys():
#    residues = c.split(",")
#    residues_all.extend(residues)
# freqs = Counter(residues_all)

# issue: are "167(HIS)" and "50(HIS)" different? they're counted as different for the above code
# print(freqs)

# same as above but counts all numbers associated with one residue as being the same residue
residues_all = []
for c in unique_chains.keys():
    residues = c.split(",")
    # gets rid of number and parentheses, just keeps 3 letter residue code
    residues = [r[r.find("(")+1:r.find(")")] for r in residues]
    residues_all.extend(residues)
freqs = Counter(residues_all)
#print(freqs)

outfile = open("frequencies.txt", "w")
for r in freqs.keys():
    outfile.write(str(r) + " " + str(freqs[r]) + "\n")
outfile.close()
