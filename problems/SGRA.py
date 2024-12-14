"""Using the Spectrum Graph to Infer Peptides.

Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any
one of them). Consult the monoisotopic mass table.
"""

from itertools import permutations
from math import isclose


def get_aa(w, aa2weight):
    for aa, weight in aa2weight.items():
        if isclose(w, weight, abs_tol=1e-3):
            return aa
    return None


data = """\
3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025
"""

aa2weight = {}
with open('constants/aa_weights.txt') as file:
    for line in file:
        aa, weight = line.split()
        aa2weight[aa] = float(weight)

weights = [float(weight) for weight in data.split()]

graph = {index: [] for index in range(len(weights))}
for index1, index2 in permutations(range(len(weights)), 2):
    weight1, weight2 = weights[index1], weights[index2]
    if weight2 < weight1:
        continue
    aa = get_aa(weight2 - weight1, aa2weight)
    if aa is not None:
        graph[index1].append((index2, aa))

peptides = []

index = min(range(len(weights)), key=lambda x: weights[x])
stack = [(index, [])]
while stack:
    index1, peptide1 = stack.pop()
    edges = graph[index1]
    if edges:
        for index2, aa in graph[index1]:
            peptide2 = peptide1.copy()
            peptide2.append(aa)
            stack.append((index2, peptide2))
    else:
        peptides.append(''.join(peptide1))

print(max(peptides, key=len))
