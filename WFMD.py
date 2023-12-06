"""The Wright-Fisher Model of Genetic Drift."""

from math import comb

import numpy as np

N, m, g, k, = 6, 9, 6, 6

P = np.zeros((2*N+1, 2*N+1))
for i in range(2*N+1):
    for j in range(2*N+1):
        p = i / (2*N)
        P[i, j] = comb(2*N, j) * p ** j * (1 - p) ** (2*N - j)

M = np.identity(2*N+1)
for _ in range(g):
    M = np.matmul(M, P)

x = np.zeros((1, 2*N+1))
x[0, m] = 1

y = np.matmul(x, M)
print(sum(y[0, :2*N-k+1]))
