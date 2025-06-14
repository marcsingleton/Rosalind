"""Consensus and Profile.

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you
may return any one of them.)

Sample input:
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample output:
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

fasta = list(parse_fasta(StringIO(data)))

profile = []
consensus = []
for i in range(len(fasta[0][1])):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(len(fasta)):
        counts[fasta[j][1][i]] += 1
    profile.append(counts)
    consensus.append(max(counts, key=lambda x: counts[x]))

print(''.join(consensus))
for sym in ('A', 'C', 'G', 'T'):
    print(sym, ': ', ' '.join([str(counts[sym]) for counts in profile]), sep='')
