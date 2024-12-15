"""Counting Point Mutations.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample input:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample output:
7
"""

seq1 = 'GAGCCTACTAACGGGAT'
seq2 = 'CATCGTAATGACGGCCT'

d = 0
for sym1, sym2 in zip(seq1, seq1):
    d += 0 if sym1 == sym2 else 1

print(d)
