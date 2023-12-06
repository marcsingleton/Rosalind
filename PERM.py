"""Enumerating Gene Orders."""

from itertools import permutations

n = 7

items = [str(i) for i in range(1, n+1)]
perms = list(permutations(items))

print(len(perms))
for perm in perms:
    print(' '.join(perm))
