"""Interleaving Two Motifs

Given: Two DNA strings s and t.

Return: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.

Sample input:
ATCTGAT
TGCATA

Sample output:
ATGCATGAT
"""

seq0 = 'ATCTGAT'
seq1 = 'TGCATA'

array = [['' for _ in range(len(seq1) + 1)] for _ in range(len(seq0) + 1)]
for i in range(1, len(seq0) + 1):
    for j in range(1, len(seq1) + 1):
        if seq0[i - 1] == seq1[j - 1]:
            array[i][j] = array[i - 1][j - 1] + seq0[i - 1]
        else:
            array[i][j] = max(array[i - 1][j], array[i][j - 1], key=len)

i = 0
j = 0
result = []
for sym in array[len(seq0)][len(seq1)]:
    while sym != seq0[i]:
        result.append(seq0[i])
        i += 1
    while sym != seq1[j]:
        result.append(seq1[j])
        j += 1
    result.append(sym)
    i += 1
    j += 1
result.extend(seq0[i:])
result.extend(seq1[j:])

print(''.join(result))
