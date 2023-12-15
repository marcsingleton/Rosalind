"""Counting Rooted Binary Trees

Given: A positive integer n (n ≤ 1000).

Return: Let B(n) represent the total number of distinct rooted binary trees on n labeled taxa. The value of b(n) modulo
1,000,000.
"""

n = 879
mod = int(1E6)

# This is effectively the same solution as CUNR, but with adding one to n
# This works because any rooted tree can be made into an unrooted tree by adding a "dummy" leaf to the root
e = 2 * n - 3
b = 1
for i in range(e, 1, -2):
    b *= i
    b %= mod

print(b)
