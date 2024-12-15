"""Independent Alleles.

Given: Two positive integers k (k ≤ 7) and N (N ≤ 2k). In this problem, we begin with Tom, who in the 0th generation has
genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't
count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

Sample input:
2 1

Sample output:
0.684
"""

from math import comb

k = 2
N = 1

# No matter the genotype of the parent, probability of double het is always 25%
p = 0.25
max_k = 2**k
pmfs = []
for i in range(max_k + 1):
    pmf = comb(max_k, i) * p**i * (1 - p) ** (max_k - i)
    pmfs.append(pmf)

q = sum(pmfs[N:])
print(q)
