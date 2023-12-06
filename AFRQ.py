"""Counting Disease Carriers.

Given: An array A for which A[k] represents the proportion of homozygous recessive individuals for the k -th Mendelian
factor in a diploid population. Assume that the population is in genetic equilibrium for all factors.

Return: An array B having the same length as A in which B[k] represents the probability that a randomly selected
individual carries at least one copy of the recessive allele for the k-th factor.
"""

A = '0.894036442942 0.869102143488 0.252238251053 0.66865599325 0.808368277717 0.563168132327 0.115105094119 0.640188077271 0.0568503630387 0.659115943386 0.389180923407 0.638582845865 0.840122545853 0.41715261345 0.0869021525488 0.79999618871 0.341170661215 0.729270244783 0.676681710399'

A = [float(a) for a in A.split()]

B = []
for a in A:
    p = a ** 0.5
    b = a + 2 * p * (1 - p)
    B.append(b)

print(' '.join([str(b) for b in B]))
