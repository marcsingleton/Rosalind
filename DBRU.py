"""Constructing a De Bruijn Graph.

Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding
to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.
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
    kmer1, kmer2 = seq[:-1], seq[1:]
    if kmer1 not in graph:
        graph[kmer1] = {kmer2}
    else:
        graph[kmer1].add(kmer2)
    if kmer2 not in graph:
        graph[kmer2] = set()

for node1, adjs in graph.items():
    for node2 in adjs:
        print(f'({node1}, {node2})')
