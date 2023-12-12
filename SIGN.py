"""Enumerating Oriented Gene Orderings.

Given: A positive integer n ≤ 6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list
the signed permutations in any order).
"""

from itertools import permutations, product

n = 5

items = [str(i) for i in range(1, n+1)]
signs = ['', '-']

perms = []
for item_perm in permutations(items):
    for sign_comb in product(*[signs for _ in range(n)]):
        perm = tuple(s + i for i, s in zip(item_perm, sign_comb))
        perms.append(perm)

print(len(perms))
for perm in perms:
    print(' '.join(perm))
