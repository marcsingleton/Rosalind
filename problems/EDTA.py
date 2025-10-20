"""Edit Distance Alignment

Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).

Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.

Sample input:
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN

Sample output:
4
PRETTY--
PR-TTEIN
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN
"""

fasta = list(parse_fasta(StringIO(data)))

s = fasta[0][1]
t = fasta[1][1]

N = len(s)
M = len(t)

dp = [[(0, None) for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = (i, (-1, 0))
for j in range(1, M + 1):
    dp[0][j] = (j, (0, -1))
for i in range(1, N + 1):
    for j in range(1, M + 1):
        v1 = (dp[i - 1][j][0] + 1, (-1, 0))
        v2 = (dp[i][j - 1][0] + 1, (0, -1))
        v3 = (dp[i - 1][j - 1][0] + int(s[i - 1] != t[j - 1]), (-1, -1))
        vs = [v1, v2, v3]
        dp[i][j] = min(vs, key=lambda x: x[0])

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

print(dp[N][M][0])
print(u)
print(v)
