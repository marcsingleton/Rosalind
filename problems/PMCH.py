"""Perfect Matchings and RNA Secondary Structures.

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number
of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

Sample input:
>Rosalind_23
AGCUAGUCAU

Sample output:
12
"""

from io import StringIO
from math import factorial

from utils import parse_fasta

data = """\
>Rosalind_23
AGCUAGUCAU
"""

fasta = list(parse_fasta(StringIO(data)))

_, seq = fasta[0]

counts = {sym: 0 for sym in 'ACGU'}
for sym in seq:
    counts[sym] += 1

if counts['A'] != counts['U'] or counts['C'] != counts['G']:
    raise RuntimeError

pAU = factorial(counts['A'])
pCG = factorial(counts['C'])
print(pAU * pCG)
