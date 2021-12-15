#!/usr/bin/env python

import os

os.system("python3 downloadPDB.py a_b_hydrolase_100.txt")
for protein in open("a_b_hydrolase_100.txt").read().split():
    os.system("python3 aminoAcidCounter.py " + protein+".cif")
    #if not os.path.isfile(os.path.join("freqplots", protein+"FreqPlot.png")):
    os.system("python3 makeFreqPlot.py frequencies.txt " + protein+"FreqPlot.png")