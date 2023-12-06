"""k-Mer Composition.

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
"""

import os
from itertools import product

import numpy as np
from utils import read_fasta

data = """\
>Rosalind_6431
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
"""
k = 4

data_path = 'KMER.txt'
with open(data_path, 'w') as file:
    file.write(data)

fasta = list(read_fasta(data_path))
_, seq = fasta[0]

alphabet = list(set(seq))

kmer2index = {}
for index, kmer in enumerate(sorted(product(*[alphabet for _ in range(k)]))):
    kmer2index[kmer] = index

array = np.zeros(len(kmer2index), dtype=int)
for i in range(len(seq) - k + 1):
    kmer = seq[i:i+k]
    index = kmer2index[tuple(kmer)]
    array[index] += 1

print(' '.join([str(value) for value in array]))

os.remove(data_path)
