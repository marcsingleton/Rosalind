"""Genome Assembly with Perfect Coverage.

Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this
dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one
simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic
chromosome).
"""

data = """\
ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT
"""

seqs = data.rstrip('\n').split('\n')

graph = {}
for seq in seqs:
    kmer1, kmer2 = seq[:-1], seq[1:]
    if kmer1 not in graph:
        graph[kmer1] = {kmer2}
    else:
        graph[kmer1].add(kmer2)
    if kmer2 not in graph:
        graph[kmer2] = set()

kmer0 = seqs[0][:-1]
kmer = list(graph[kmer0])[0]
chromosome = [kmer[-1]]
while kmer != kmer0:
    kmer = list(graph[kmer])[0]
    chromosome.append(kmer[-1])

print(''.join(chromosome))
