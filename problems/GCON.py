"""Global Alignment with Constant Gap Penalty.

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The maximum alignment score between s and t. Use:
- The BLOSUM62 scoring matrix.
- Constant gap penalty equal to 5.

Sample input:
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY

Sample output:
13
"""

from io import StringIO
from math import inf

from utils import parse_fasta

data = """\
>Rosalind_79
PLEASANTLY
>Rosalind_41
MEANLY
"""

GAP = -5

fasta = list(parse_fasta(StringIO(data)))

s = fasta[0][1]
t = fasta[1][1]

S = {}
with open('constants/BLOSUM62.txt') as file:
    syms_j = file.readline().split()
    for line in file:
        fields = line.split()
        sym_i = fields[0]
        scores = fields[1:]
        Si = {sym: int(score) for sym, score in zip(syms_j, scores)}
        S[sym_i] = Si

N = len(s)
M = len(t)

L = [[-inf for j in range(M + 1)] for i in range(N + 1)]  # Ends in match
X = [[-inf for j in range(M + 1)] for i in range(N + 1)]  # Ends in gap in s
Y = [[-inf for j in range(M + 1)] for i in range(N + 1)]  # Ends in gap in t
L[0][0] = 0
for i in range(1, N + 1):
    Y[i][0] = GAP
for j in range(1, M + 1):
    X[0][j] = GAP
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sym_s = s[i - 1]
        sym_t = t[j - 1]

        v1 = L[i - 1][j - 1] + S[sym_s][sym_t]
        v2 = X[i - 1][j - 1] + S[sym_s][sym_t]
        v3 = Y[i - 1][j - 1] + S[sym_s][sym_t]
        vs = [v1, v2, v3]
        L[i][j] = max(vs)

        v1 = L[i][j - 1] + GAP
        v2 = X[i][j - 1]
        v3 = Y[i][j - 1] + GAP
        vs = [v1, v2, v3]
        X[i][j] = max(vs)

        v1 = L[i - 1][j] + GAP
        v2 = X[i - 1][j] + GAP
        v3 = Y[i - 1][j]
        vs = [v1, v2, v3]
        Y[i][j] = max(vs)

print(max(dp[N][M] for dp in [L, X, Y]))
