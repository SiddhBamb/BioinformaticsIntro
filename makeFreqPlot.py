import collections
import os
import argparse
import matplotlib.pyplot as plt
import seaborn as sns

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

total = sum([int(f) for f in freqs])

freqdict = {}
for i in range(len(residues)):
    freqdict[residues[i]] = freqs[i]
# alphabetize the dictionary of frequencies of residues
freqdict = {x:int(freqdict[x]) for x in sorted(freqdict)}
percentages = [round(x/total*100,2) for x in freqdict.values()]

# use matplotlib to plot it as a histogram, saving to the desired path
if not os.path.isdir("freqplots"):
    os.mkdir("freqplots")
plt.title(args.outfile[:args.outfile.find(".")])
plt.xlabel("Residue")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(which='major', axis="y", color="#555555", linewidth=0.8)
plt.grid(which='minor', axis="y", color="#888888", linewidth=0.4)
plt.minorticks_on()
plt.bar(freqdict.keys(), freqdict.values())
plt.savefig(os.path.join("freqplots",args.outfile))
