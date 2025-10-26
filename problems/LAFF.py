"""Local Alignment with Affine Gap Penalty

Given: Two protein strings s and t in FASTA format (each having length at most 10,000 aa).

Return: Return: The maximum local alignment score of s and t, followed by substrings r and u of s and t, respectively,
that correspond to the optimal local alignment of s and t. Use:
 - The BLOSUM62 scoring matrix.
 - Gap opening penalty equal to 11.
 - Gap extension penalty equal to 1.

Sample input:
>Rosalind_8
PLEASANTLY
>Rosalind_18
MEANLY

Sample output:
12
LEAS
MEAN
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_8
PLEASANTLY
>Rosalind_18
MEANLY
"""

GAP_OPEN = -11
GAP_EXTEND = -1

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

L = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]  # Ends in match
X = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]  # Ends in gap in s
Y = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]  # Ends in gap in t
# L[0][0] = (0, None)
# for i in range(1, N + 1):
#     Y[i][0] = (GAP_OPEN + (i - 1) * GAP_EXTEND, (-1, 0, 2))
# for j in range(1, M + 1):
#     X[0][j] = (GAP_OPEN + (j - 1) * GAP_EXTEND, (0, -1, 1))
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sym_s = s[i - 1]
        sym_t = t[j - 1]

        v1 = (L[i - 1][j - 1][0] + S[sym_s][sym_t], (-1, -1, 0))
        v2 = (X[i - 1][j - 1][0] + S[sym_s][sym_t], (-1, -1, 1))
        v3 = (Y[i - 1][j - 1][0] + S[sym_s][sym_t], (-1, -1, 2))
        v4 = (0, None)
        vs = [v1, v2, v3, v4]
        L[i][j] = max(vs, key=lambda x: x[0])

        v1 = (L[i][j - 1][0] + GAP_OPEN, (0, -1, 0))
        v2 = (X[i][j - 1][0] + GAP_EXTEND, (0, -1, 1))
        v3 = (Y[i][j - 1][0] + GAP_OPEN, (0, -1, 2))
        v4 = (0, None)
        vs = [v1, v2, v3, v4]
        X[i][j] = max(vs, key=lambda x: x[0])

        v1 = (L[i - 1][j][0] + GAP_OPEN, (-1, 0, 0))
        v2 = (X[i - 1][j][0] + GAP_OPEN, (-1, 0, 1))
        v3 = (Y[i - 1][j][0] + GAP_EXTEND, (-1, 0, 2))
        v4 = (0, None)
        vs = [v1, v2, v3, v4]
        Y[i][j] = max(vs, key=lambda x: x[0])

dps = [L, X, Y]
v = 0
x, y, z = 0, 0, 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for k in range(len(dps)):
            if dps[k][i][j][0] > v:
                v = dps[k][i][j][0]
                x, y, z = i, j, k

u = []
v = []

i = x
j = y
k = z
while i != 0 or j != 0:
    di, dj, k = dps[k][i][j][1]
    if di == -1:
        u.append(s[i - 1])
    if dj == -1:
        v.append(t[j - 1])
    i += di
    j += dj
    if dps[k][i][j][0] == 0:
        break
u = ''.join(u[::-1])
v = ''.join(v[::-1])

print(dps[z][x][y][0])
print(u)
print(v)
