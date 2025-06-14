"""Genome Assembly as Shortest Superstring.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads
deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample input:
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample output:
ATTAGACCTGCCGGAATAC
"""

from io import StringIO
from itertools import permutations
from math import ceil

from utils import parse_fasta


def has_overlap(s1, s2, r):
    max_i = ceil(r * len(s1))
    min_i = max(0, len(s1) - len(s2))
    for i in range(min_i, max_i):
        s1_suffix = s1[i:]
        s2_prefix = s2[: len(s1) - i]
        if s1_suffix == s2_prefix:
            return i
    return -1


data = """\
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC
"""

r = 0.5

fasta = dict(parse_fasta(StringIO(data)))

graph = {header: [] for header in fasta}
for (header1, seq1), (header2, seq2) in permutations(fasta.items(), 2):
    index = has_overlap(seq1, seq2, r)
    if index >= 0:
        graph[header1].append((header2, index))

counts = {header: 0 for header in fasta}
for edges in graph.values():
    for header, _ in edges:
        counts[header] += 1

superstrings = []
start_headers = [header for header, count in counts.items() if count == 0]
for start_header in start_headers:
    prefixes = []

    header1 = start_header
    seq = fasta[header1]
    edges = graph[header1]
    while edges:
        header2, index = edges.pop()
        prefixes.append(seq[:index])

        header1 = header2
        seq = fasta[header1]
        edges = graph[header1]
    prefixes.append(seq)
    superstrings.append(''.join(prefixes))

for superstring in superstrings:
    print(superstring)
