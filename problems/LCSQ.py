"""Finding a Shared Spliced Motif.

Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)

Sample input:
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA

Sample output:
AACTGG
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA
"""

fasta = list(parse_fasta(StringIO(data)))

seq0 = fasta[0][1]
seq1 = fasta[1][1]

array = [['' for _ in range(len(seq1) + 1)] for _ in range(len(seq0) + 1)]
for i in range(1, len(seq0) + 1):
    for j in range(1, len(seq1) + 1):
        if seq0[i - 1] == seq1[j - 1]:
            array[i][j] = array[i - 1][j - 1] + seq0[i - 1]
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1], key=len)

print(array[len(seq0)][len(seq1)])
