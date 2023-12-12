"""Counting Subsets.

Given: A positive integer n (n ≤ 1000).

Return: The total number of subsets of {1, 2, …, n} modulo 1,000,000.
"""

n = 850

total = 1
for _ in range(n):
    total = 2 * total % 1E6
print(total)