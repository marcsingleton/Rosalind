"""Counting Quartets.

Given: A positive integer n (4 ≤ n ≤ 5000), followed by an unrooted binary tree T in Newick format on n taxa.

Return: Let q(T) denote the total number of quartets that are consistent with T. The value of q(T) modulo 1,000,000.

Sample input:
6
(lobster,(cat,dog),(caterpillar,(elephant,mouse)));

Sample output:
15
"""

from math import comb

data = """\
6
(lobster,(cat,dog),(caterpillar,(elephant,mouse)));
"""
mod = int(1e6)

lines = data.rstrip('\n').split('\n')
n = int(lines[0])

print(comb(n, 4) % mod)
