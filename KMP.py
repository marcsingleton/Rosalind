"""Speeding Up Motif Finding

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
"""

import os

from utils import read_fasta

data = """\
>Rosalind_87
CAGCATGGTATCACAGCAGAG
"""

data_path = 'LCSM.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

header, seq = fasta[0]

array = [0 for _ in seq]
for j in range(1, len(seq)):
    value = array[j-1]
    for i in range(value+1, 0, -1):
        prefix = seq[:i]
        suffix = seq[j+1-i:j+1]
        if prefix == suffix:
            array[j] = i
            break

print(' '.join([str(value) for value in array]))
