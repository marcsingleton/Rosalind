"""Genome Assembly Using Reads.

Given: A collection S of (error-free) reads of equal length (not exceeding 50 bp). In this dataset, for some positive
integer k, the de Bruijn graph Bk on Sk+1∪Srck+1 consists of exactly two directed cycles.

Return: A cyclic superstring of minimal length containing every read or its reverse complement.

Sample input:
AATCT
TGTAA
GATTA
ACAGA

Sample output:
GATTACA
"""

from utils import reverse_complement

data = """\
AATCT
TGTAA
GATTA
ACAGA
"""

seqs = data.rstrip('\n').split('\n')
seqs = seqs + [reverse_complement(seq) for seq in seqs]

max_k = min([len(seq) for seq in seqs]) - 1
for k in range(max_k, 0, -1):
    kmers = []
    for seq in seqs:
        for i in range(len(seq) - k):
            kmers.append(seq[i : i + k + 1])

    graph = {}
    for kmer in kmers:
        prefix, suffix = kmer[:-1], kmer[1:]
        if prefix not in graph:
            graph[prefix] = {suffix}
        else:
            graph[prefix].add(suffix)
        if suffix not in graph:
            graph[suffix] = set()

    prefix0 = list(graph)[0]
    prefixes = list(graph[prefix0])
    if not prefixes:
        continue
    prefix = prefixes[0]
    chromosome = [prefix[-1]]
    visited = set()
    while prefix != prefix0 and prefix not in visited:
        visited.add(prefix)
        prefixes = list(graph[prefix])
        if not prefixes:
            break
        prefix = prefixes[0]
        chromosome.append(prefix[-1])

    if prefix == prefix0:
        print('k =', k)
        print(''.join(chromosome))
        print()
