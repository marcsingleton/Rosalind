"""Counting Disease Carriers.

Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k -th Mendelian
factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected
individual carries at least one copy of the recessive allele for the k-th factor.
"""

A = '0.1 0.25 0.5'

A = [float(a) for a in A.split()]

B = []
for a in A:
    p = a ** 0.5
    b = a + 2 * p * (1 - p)
    B.append(b)

print(' '.join([str(b) for b in B]))
