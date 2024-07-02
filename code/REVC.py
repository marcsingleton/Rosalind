"""Complementing a Strand of DNA.

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

from utils import reverse_complement

seq = 'AAAACCCGGT'

pairs = [('A', 'T'), ('G', 'C')]
table = {**{ord(b1): ord(b2) for b1, b2 in pairs}, **{ord(b2): ord(b1) for b1, b2 in pairs}}
print(reverse_complement(seq))
