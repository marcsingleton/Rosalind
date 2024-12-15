"""Partial Permutations.

Given: Positive integers n and k such that 100 ≥ n > 0 and 10 ≥ k > 0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

Sample input:
21 7

Sample output:
51200
"""

from math import comb, perm

n, k = 21, 7
mod = int(1e6)

c = comb(n, k) % mod
p = perm(k, k) % mod
cp = c * p % mod
print(cp)
