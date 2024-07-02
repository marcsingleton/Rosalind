"""Ordering Strings of Varying Length Lexicographically.

Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n ( n≤ 4).

Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers
Lexicographically”, alphabet order is based on the order in which the symbols are given.)
"""

from itertools import product

alphabet = 'V L B D I Y T Z X G E'
n = 4

alphabet = alphabet.split()
order = {sym: i for i, sym in enumerate(alphabet)}

perms = []
for k in range(1, n+1):
    for perm in product(*[alphabet for i in range(k)]):
        perms.append(perm)

for perm in sorted(perms, key=lambda xs: [order[x] for x in xs]):
    print(''.join(perm))
