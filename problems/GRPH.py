"""Overlap Graphs.

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample input:
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample output:
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

from io import StringIO

from utils import parse_fasta

data = """\
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""

fasta = list(parse_fasta(StringIO(data)))

for header1, seq1 in fasta:
    for header2, seq2 in fasta:
        if header1 == header2:
            continue
        elif seq1[-3:] == seq2[:3]:
            print(header1, header2)
