"""Locating Restriction Sites.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return
these pairs in any order.

Sample input:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""

from io import StringIO

import numpy as np
from utils import parse_fasta

data = """\
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

pairs = [('A', 'T'), ('G', 'C')]
complements = {}
for sym1, sym2 in pairs:
    complements[sym1] = sym2
    complements[sym2] = sym1

fasta = list(parse_fasta(StringIO(data)))

header, seq = fasta[0]

# Initialize DP array
n = len(seq)
array = np.zeros((n, n), dtype=bool)
for i in range(n - 1):
    sym1, sym2 = seq[i], seq[i + 1]
    if sym1 == complements[sym2]:
        array[i, i + 1] = True

# Fill DP array along diagonals
for delta in range(2, n):
    for j in range(delta, n):
        i = j - delta
        sym1, sym2 = seq[i], seq[j]
        if sym1 == complements[sym2] and array[i + 1, j - 1]:
            array[i, j] = True

# Iterate over DP array and print results
for i in range(n):
    for j in range(i, n):
        if array[i, j] and 4 <= j - i + 1 <= 12:
            print(i + 1, j - i + 1)
