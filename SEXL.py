"""Sex-Linked Inheritance.

Given: An array A of length n for which A[k] represents the proportion of males in a population exhibiting the k-th of n
total recessive X-linked genes. Assume that the population is in genetic equilibrium for all n genes.

Return: An array B of length n in which B[k] equals the probability that a randomly selected female will be a carrier
for the k-th gene.
"""

A = '0.130598752791 0.161170280809 0.181064158778 0.203803284559 0.257175293744 0.405026595264 0.444171274072 0.452864336912 0.495615954178 0.569224225179 0.688921512369 0.774025275787 0.779174654501 0.801915466664 0.802546280447 0.889050723813 0.994699829851'

A = [float(a) for a in A.split()]

B = []
for a in A:
    b = 2 * a * (1 - a)
    B.append(b)

print(' '.join([str(b) for b in B]))
