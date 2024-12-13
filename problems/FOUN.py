"""The Founder Effect and Genetic Drift.

Given: Two positive integers N and m, followed by an array A containing k integers between 0 and 2N. A[j] represents the
number of recessive alleles for the j-th factor in a population of N diploid individuals.

Return: An m×k matrix B for which Bi,j represents the common logarithm of the probability that after i generations, no
copies of the recessive allele for the j-th factor will remain in the population. Apply the Wright-Fisher model.
"""

from math import comb

import numpy as np

N = 19
m = 4
A = '4 9 12'

A = [int(a) for a in A.split()]
x = np.zeros((len(A), 2*N+1))
for i, a in enumerate(A):
    x[i, a] = 1

P = np.zeros((2*N+1, 2*N+1))
for i in range(2*N+1):
    for j in range(2*N+1):
        p = i / (2*N)
        P[i, j] = comb(2*N, j) * p ** j * (1 - p) ** (2*N - j)

M = np.identity(2*N+1)
B = np.zeros((m, len(A)))
for i in range(1, m+1):
    M = np.matmul(M, P)
    b = np.matmul(x, M)
    B[i-1] = np.log10(b[:, 0])

for b in B:
    print(' '.join([str(value) for value in b]))
