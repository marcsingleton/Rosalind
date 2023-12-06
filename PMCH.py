"""Perfect Matchings and RNA Secondary Structures."""

import os
from math import factorial

from utils import read_fasta


data = """\
>Rosalind_0690
UCCCAAGAUAGCGGGUUCGAUGCAAAAAAAUAAGGUUCUGGCAACGAGUCUUGCCUGUUG
CCUCUACAGCUCCUGCUGAG
"""

data_path = 'PMCH.txt'
with open(data_path, 'w') as file:
    file.write(data)

fasta = list(read_fasta(data_path))
_, seq = fasta[0]

counts = {sym: 0 for sym in 'ACGU'}
for sym in seq:
    counts[sym] += 1

if counts['A'] != counts['U'] or counts['C'] != counts['G']:
    raise RuntimeError

pAU = factorial(counts['A'])
pCG = factorial(counts['C'])
print(pAU * pCG)

os.remove(data_path)
