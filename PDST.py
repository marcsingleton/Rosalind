"""Creating a Distance Matrix.

Given: A collection of n (n ≤ 10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA
format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is
allowed an absolute error of 0.001.
"""

import os
from itertools import product

import numpy as np
from utils import read_fasta

data = """\
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA
"""

data_path = 'PDST.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

indices = {seq_id: index for index, (seq_id, _) in enumerate(fasta)}

array = np.zeros((len(fasta), len(fasta)))
for (seq_id1, seq1), (seq_id2, seq2) in product(fasta, fasta):
    i, j = indices[seq_id1], indices[seq_id2]
    equal = [sym1 != sym2 for sym1, sym2 in zip(seq1, seq2)]
    pdist = sum(equal) / len(equal)
    array[i, j] = pdist
    array[j, i] = pdist

for row in array:
    print(' '.join([str(value) for value in row]))
