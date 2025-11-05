"""Semiglobal Alignment

Given: Two DNA strings s and t in FASTA format, each having length at most 10 kbp.

Return: The maximum semiglobal alignment score of s and t, followed by an alignment of s and t achieving this maximum
score. Use an alignment score in which matching symbols count +1, substitutions count -1, and there is a linear gap
penalty of 1. If multiple optimal alignments exist, then you may return any one.

Sample input:
>Rosalind_79
CAGCACTTGGATTCTCGG
>Rosalind_98
CAGCGTGG

Sample output:
4
CAGCA-CTTGGATTCTCGG
---CAGCGTGG--------
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_79
CAGCACTTGGATTCTCGG
>Rosalind_98
CAGCGTGG
"""

GAP = -1

fasta = list(parse_fasta(StringIO(data)))

s = fasta[0][1]
t = fasta[1][1]

N = len(s)
M = len(t)

dp = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = (0, (-1, 0))
for j in range(1, M + 1):
    dp[0][j] = (0, (0, -1))
for i in range(1, N + 1):
    for j in range(1, M + 1):
        S = 1 if s[i - 1] == t[j - 1] else -1
        G1 = 0 if j == M else GAP
        G2 = 0 if i == N else GAP
        v1 = (dp[i - 1][j][0] + G1, (-1, 0))
        v2 = (dp[i][j - 1][0] + G2, (0, -1))
        v3 = (dp[i - 1][j - 1][0] + S, (-1, -1))
        vs = [v1, v2, v3]
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
i = N
j = M
while i != 0 or j != 0:
    di, dj = dp[i][j][1]
    if di == -1:
        u.append(s[i - 1])
    else:
        u.append('-')
    if dj == -1:
        v.append(t[j - 1])
    else:
        v.append('-')
    i += di
    j += dj
u = ''.join(u[::-1])
v = ''.join(v[::-1])

print(dp[x][y][0])
print(u)
print(v)
