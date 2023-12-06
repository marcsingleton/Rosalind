"""Partial Permutations."""

from math import comb, perm

n, k = 96, 8
mod = 1E6


c = comb(n, k) % mod
p = perm(k, k) % mod
cp = c * p % mod
print(cp)
