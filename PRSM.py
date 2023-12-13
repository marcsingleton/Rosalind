"""Matching a Spectrum to a Protein."""

from itertools import product


def make_multiset(values):
    multiset = {}
    for value in values:
        multiset[value] = 1 + multiset.get(value, 0)
    return multiset


data = """\
4
GSDMQS
VWICN
IASWMQS
PVSMGAD
445.17838
115.02694
186.07931
314.13789
317.1198
215.09061
"""

aa2weight = {}
with open('constants/aa_weights.txt') as file:
    for line in file:
        aa, weight = line.split()
        aa2weight[aa] = float(weight)

lines = data.rstrip('\n').split('\n')
n = int(lines[0])
seqs = lines[1:n+1]
reference = [float(line) for line in lines[n+1:]]

spectra = []
for seq in seqs:
    spectrum = []
    for i in range(len(seq)+1):
        prefix = seq[:i]
        suffix = seq[i:]
        prefix_weight = sum([aa2weight[aa] for aa in prefix])
        suffix_weight = sum([aa2weight[aa] for aa in suffix])
        spectrum.extend([prefix_weight, suffix_weight])
    spectra.append(spectrum)

msets = []
for spectrum in spectra:
    diffs = []
    for value1, value2 in product(reference, spectrum):
        diff = round(value1 - value2, 5)
        diffs.append(diff)
    mset = make_multiset(diffs)
    msets.append(mset)

index = max(range(len(msets)), key=lambda x: max(msets[x].values()))
print(max(msets[index].values()))
print(seqs[index])
