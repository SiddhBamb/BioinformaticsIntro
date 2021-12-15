import collections
import argparse
import matplotlib.pyplot as plt

# read in the path of the freq text file to plot
parser = argparse.ArgumentParser(description="plot frequency histogram with the given data")
parser.add_argument('infile', help="input frequencies file")
parser.add_argument('outfile', help="input frequencies file")
args = parser.parse_args()

# read file and load it into a dictionary
file = open(args.infile, "r")
data = file.read().split()
residues = data[::2]
freqs = data[1::2]
freqdict = {}
for i in range(len(residues)):
    freqdict[residues[i]] = freqs[i]
# alphabetize the dictionary of frequencies of residues
freqdict = {x:int(freqdict[x]) for x in sorted(freqdict)}

# use matplotlib to plot it as a histogram, saving to the desired path
plt.xlabel("Residue")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(which='major', axis="y", color="#555555", linewidth=0.8)
plt.grid(which='minor', axis="y", color="#888888", linewidth=0.4)
plt.minorticks_on()
plt.bar(freqdict.keys(), freqdict.values())
plt.savefig(args.outfile)