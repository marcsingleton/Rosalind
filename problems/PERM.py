"""Enumerating Gene Orders.

Given: A positive integer n ≤ 7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample input:
3

Sample output:
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

from itertools import permutations

n = 3

items = [str(i) for i in range(1, n + 1)]
perms = list(permutations(items))

print(len(perms))
for perm in perms:
    print(' '.join(perm))
