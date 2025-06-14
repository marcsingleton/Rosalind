"""Speeding Up Motif Finding

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.

Sample input:
>Rosalind_87
CAGCATGGTATCACAGCAGAG

Sample output:
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_87
CAGCATGGTATCACAGCAGAG
"""

fasta = list(parse_fasta(StringIO(data)))

header, seq = fasta[0]

array = [0 for _ in seq]
for j in range(1, len(seq)):
    value = array[j - 1]
    for i in range(value + 1, 0, -1):
        prefix = seq[:i]
        suffix = seq[j + 1 - i : j + 1]
        if prefix == suffix:
            array[j] = i
            break

print(' '.join([str(value) for value in array]))
