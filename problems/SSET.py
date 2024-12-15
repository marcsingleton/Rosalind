"""Counting Subsets.

Given: A positive integer n (n ≤ 1000).

Return: The total number of subsets of {1, 2, …, n} modulo 1,000,000.

Sample input:
3

Sample output:
8
"""

n = 3
mod = int(1e6)

total = 1
for _ in range(n):
    total = 2 * total % mod

print(total)
