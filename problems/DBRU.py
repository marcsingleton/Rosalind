"""Constructing a De Bruijn Graph.

Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding
to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.

Sample input:
TGAT
CATG
TCAT
ATGC
CATC
CATC

Sample output:
(ATC, TCA)
(ATG, TGA)
(ATG, TGC)
(CAT, ATC)
(CAT, ATG)
(GAT, ATG)
(GCA, CAT)
(TCA, CAT)
(TGA, GAT)
"""

from utils import reverse_complement

data = """\
TGAT
CATG
TCAT
ATGC
CATC
CATC
"""

seqs = data.rstrip('\n').split('\n')
seqs = seqs + [reverse_complement(seq) for seq in seqs]

graph = {}
for seq in seqs:
    prefix, suffix = seq[:-1], seq[1:]
    if prefix not in graph:
        graph[prefix] = {suffix}
    else:
        graph[prefix].add(suffix)
    if suffix not in graph:
        graph[suffix] = set()

for node1, adjacents in graph.items():
    for node2 in adjacents:
        print(f'({node1}, {node2})')
