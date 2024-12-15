"""Sex-Linked Inheritance.

Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th of n
total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.

Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier
for the k-th gene.

Sample input:
0.1 0.5 0.8

Sample output:
0.18 0.5 0.32
"""

A = '0.1 0.5 0.8'

A = [float(a) for a in A.split()]

B = []
for a in A:
    b = 2 * a * (1 - a)
    B.append(b)

print(' '.join([str(b) for b in B]))
