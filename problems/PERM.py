"""Enumerating Gene Orders.

Given: A positive integer n ≤ 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""

from itertools import permutations

n = 7

items = [str(i) for i in range(1, n + 1)]
perms = list(permutations(items))

print(len(perms))
for perm in perms:
    print(' '.join(perm))
