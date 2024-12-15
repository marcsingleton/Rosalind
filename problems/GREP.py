"""Genome Assembly with Perfect Coverage and Repeats.

Given: A list Sk+1 of error-free DNA (k+1)-mers (k ≤ 5) taken from the same strand of a circular chromosome (of
length ≤ 50).

Return: All circular strings assembled by complete cycles in the de Bruijn graph Bk of Sk+1. The strings may be given in
any order, but each one should begin with the first (k+1)-mer provided in the input.

Sample input:
CAG
AGT
GTT
TTT
TTG
TGG
GGC
GCG
CGT
GTT
TTC
TCA
CAA
AAT
ATT
TTC
TCA

Sample output:
CAGTTCAATTTGGCGTT
CAGTTCAATTGGCGTTT
CAGTTTCAATTGGCGTT
CAGTTTGGCGTTCAATT
CAGTTGGCGTTCAATTT
CAGTTGGCGTTTCAATT
"""

from collections import Counter

data = """\
CAG
AGT
GTT
TTT
TTG
TGG
GGC
GCG
CGT
GTT
TTC
TCA
CAA
AAT
ATT
TTC
TCA
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

prefix0 = seqs[0][:-1]
prefix = seqs[0][1:]
reads = Counter(seqs[1:])
stack = [(prefix, [prefix[-1]], reads)]
for prefix, chromosome, reads in stack:
    if sum(reads.values()) == 0:
        chromosome = ''.join(chromosome)
        print(chromosome[-len(prefix0) :] + chromosome[: -len(prefix0)])
        continue
    for suffix in graph[prefix]:
        seq = prefix + suffix[-1]
        if reads[seq] > 0:
            new_reads = reads.copy()
            new_reads[seq] -= 1
            new_chromosome = chromosome.copy()
            new_chromosome.append(suffix[-1])
            stack.append((suffix, new_chromosome, new_reads))
