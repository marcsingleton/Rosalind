"""Transitions and Transversions.

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1, s2).

Sample input:
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

Sample output:
1.21428571429
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
"""

fasta = list(parse_fasta(StringIO(data)))

_, seq1 = fasta[0]
_, seq2 = fasta[1]

counts = {'TI': 0, 'TV': 0}
for sym1, sym2 in zip(seq1, seq2):
    syms = {sym1, sym2}
    if sym1 == sym2:
        continue
    elif syms == {'A', 'G'} or syms == {'C', 'T'}:
        counts['TI'] += 1
    else:
        counts['TV'] += 1

print(counts['TI'] / counts['TV'])
