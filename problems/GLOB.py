"""Global Alignment with Scoring Matrix

Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).

Return: The maximum alignment score between s and t. Use:
 - The BLOSUM62 scoring matrix.
 - Linear gap penalty equal to 5 (i.e., a cost of -5 is assessed for each gap symbol).

Sample input:
>Rosalind_67
PLEASANTLY
>Rosalind_17
MEANLY

Sample output:
8
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_67
PLEASANTLY
>Rosalind_17
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

dp = [[0 for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    dp[i][0] = i * GAP
for j in range(1, M + 1):
    dp[0][j] = j * GAP
for i in range(1, N + 1):
    for j in range(1, M + 1):
        sym_s = s[i - 1]
        sym_t = t[j - 1]
        v1 = dp[i - 1][j] + GAP
        v2 = dp[i][j - 1] + GAP
        v3 = dp[i - 1][j - 1] + S[sym_s][sym_t]
        vs = [v1, v2, v3]
        dp[i][j] = max(vs)

print(dp[N][M])
