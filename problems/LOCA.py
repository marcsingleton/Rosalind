"""Local Alignment with Scoring Matrix

Given: Two protein strings s and t in FASTA format (each having length at most 1000 aa).

Return: A maximum alignment score along with substrings r and u of s and t, respectively, which produce this maximum
alignment score (multiple solutions may exist, in which case you may output any one). Use:
 - The PAM250 scoring matrix.
 - Linear gap penalty equal to 5.

Sample input:
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN

23
LYPRTEINSTRIN
LYEINSTEIN
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_80
MEANLYPRTEINSTRING
>Rosalind_21
PLEASANTLYEINSTEIN
"""

GAP = -5

fasta = list(parse_fasta(StringIO(data)))

s = fasta[0][1]
t = fasta[1][1]

S = {}
with open('constants/PAM250.txt') as file:
    syms_j = file.readline().split()
    for line in file:
        fields = line.split()
        sym_i = fields[0]
        scores = fields[1:]
        Si = {sym: int(score) for sym, score in zip(syms_j, scores)}
        S[sym_i] = Si

N = len(s)
M = len(t)

dp = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sym_s = s[i - 1]
        sym_t = t[j - 1]
        v1 = (dp[i - 1][j][0] + GAP, (-1, 0))
        v2 = (dp[i][j - 1][0] + GAP, (0, -1))
        v3 = (dp[i - 1][j - 1][0] + S[sym_s][sym_t], (-1, -1))
        v4 = (0, None)
        vs = [v1, v2, v3, v4]
        dp[i][j] = max(vs, key=lambda x: x[0])

v = 0
x, y = 0, 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if dp[i][j][0] > v:
            v = dp[i][j][0]
            x, y = i, j

u = []
v = []
i = x
j = y
while i != 0 or j != 0:
    di, dj = dp[i][j][1]
    if di == -1:
        u.append(s[i - 1])
    if dj == -1:
        v.append(t[j - 1])
    i += di
    j += dj
    if dp[i][j][0] == 0:
        break
u = ''.join(u[::-1])
v = ''.join(v[::-1])

print(dp[x][y][0])
print(u)
print(v)
