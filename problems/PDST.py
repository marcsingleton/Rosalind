"""Creating a Distance Matrix.

Given: A collection of n (n ≤ 10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA
format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is
allowed an absolute error of 0.001.

Sample input:
>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA

Sample output:
0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000
"""

from io import StringIO
from itertools import product

import numpy as np
from utils import parse_fasta

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

fasta = list(parse_fasta(StringIO(data)))

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
