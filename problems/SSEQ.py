"""Finding a Spliced Motif.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions
exist, you may return any one.

Sample input:
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample output:
3 8 10
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA
"""

fasta = list(parse_fasta(StringIO(data)))

_, seq1 = fasta[0]
_, seq2 = fasta[1]

indices = []
seq2_index = 0
for seq1_index, sym in enumerate(seq1):
    if sym == seq2[seq2_index]:
        indices.append(seq1_index + 1)
        seq2_index += 1
    if seq2_index == len(seq2):
        break

print(' '.join(str(index) for index in indices))
