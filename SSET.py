"""Counting Subsets.

Given: A positive integer n (n ≤ 1000).

Return: The total number of subsets of {1, 2, …, n} modulo 1,000,000.
"""

n = 850
mod = int(1E6)

total = 1
for _ in range(n):
    total = 2 * total % mod

print(total)
