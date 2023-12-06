"""Enumerating k-mers Lexicographically.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n ≤ 10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order
of symbols in the English alphabet).
"""

from itertools import product

alphabet = 'A B C D E F'
n = 3

alphabet = alphabet.split()
for perm in sorted(product(*[alphabet for _ in range(n)])):
    print(''.join(perm))
