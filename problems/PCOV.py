"""Genome Assembly with Perfect Coverage.

Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this
dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one
simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic
chromosome).

Sample input:
ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT

Sample output:
GATTACA
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
    prefix, suffix = seq[:-1], seq[1:]
    if prefix not in graph:
        graph[prefix] = {suffix}
    else:
        graph[prefix].add(suffix)
    if suffix not in graph:
        graph[suffix] = set()

prefix0 = list(graph)[0]
prefix = list(graph[prefix0])[0]
chromosome = [prefix[-1]]
while prefix != prefix0:
    prefix = list(graph[prefix])[0]
    chromosome.append(prefix[-1])

print(''.join(chromosome))
