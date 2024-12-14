"""Matching Random Motifs.

Given: A positive integer N ≤ 100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see
“Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be
created more than once.
"""

N = 97023
gc = 0.515636
s = 'TCCAACATA'

ps = {
    'A': (1 - gc) / 2,
    'C': gc / 2,
    'G': gc / 2,
    'T': (1 - gc) / 2,
}

p_match = 1
for sym in s:
    p_match *= ps[sym]

q = 1 - (1 - p_match) ** N
print(q)
