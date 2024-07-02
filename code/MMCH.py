"""Maximum Matchings and RNA Secondary Structures.

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
"""

import os
from math import perm

from utils import read_fasta


data = """\
>Rosalind_8322
CAUAGUGCAGCCGUGAAGUGCCAAAGCUGGCAACGCGUUCUCCCGUACGUUGGAACUCGA
UCCGGAACUACAAUGGCACCGCGCCAUUGUCUUA
"""

data_path = 'MMCH.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

_, seq = fasta[0]

counts = {sym: 0 for sym in 'ACGU'}
for sym in seq:
    counts[sym] += 1

n, k = max(counts['A'], counts['U']), min(counts['A'], counts['U'])
pAU = perm(n, k)

n, k = max(counts['C'], counts['G']), min(counts['C'], counts['G'])
pCG = perm(n, k)

print(pAU * pCG)
