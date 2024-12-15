"""Independent Segregation of Chromosomes.

Given: A positive integer n ≤5 0.

Return: An array A of length 2n in which A[k] represents the common logarithm of the probability that two diploid
siblings share at least k of their 2n chromosomes (we do not consider recombination for now).

Sample input:
5

Sample output:
0.000 -0.004 -0.024 -0.082 -0.206 -0.424 -0.765 -1.262 -1.969 -3.010
"""

from math import comb, log10

n = 5
p = 0.5

qs = [comb(2 * n, k) * p ** (2 * n) for k in range(2 * n + 1)]
A = []
for i in range(1, 2 * n + 1):
    a = log10(sum(qs[i:]))
    A.append(a)

print(' '.join([str(a) for a in A]))
