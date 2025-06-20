"""Edit Distance.

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The edit distance dE(s,t).

Sample input:
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY

Sample output:
5
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_39
PLEASANTLY
>Rosalind_11
MEANLY
"""

fasta = list(parse_fasta(StringIO(data)))

seq0 = fasta[0][1]
seq1 = fasta[1][1]

array = [[0 for _ in range(len(seq1) + 1)] for _ in range(len(seq0) + 1)]
for i in range(len(seq0) + 1):
    for j in range(len(seq1) + 1):
        if i == 0:
            array[0][j] = j
        elif j == 0:
            array[i][0] = i
        elif seq0[i - 1] == seq1[j - 1]:
            array[i][j] = array[i - 1][j - 1]
        else:
            array[i][j] = 1 + min(array[i - 1][j - 1], array[i - 1][j], array[i][j - 1])

min_edits = array[len(seq0)][len(seq1)]
print(min_edits)
