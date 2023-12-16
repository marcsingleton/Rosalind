"""RNA Splicing.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are
given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist
for the dataset provided.)
"""

import os

from utils import read_fasta

data = """\
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""

data_path = 'SPLC.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

_, seq = fasta[0]
for _, intron in fasta[1:]:
    index = seq.find(intron)
    seq = seq[:index] + seq[index+len(intron):]
seq = seq.replace('T', 'U')

gencode = {}
with open('constants/codons.txt') as file:
    for line in file:
        keyvals = line.rstrip('\n').split('\t')
        for keyval in keyvals:
            codon, aa = keyval.split()
            gencode[codon] = aa

aas = []
for i in range(0, len(seq) - 3, 3):
    codon = seq[i:i+3]
    aas.append(gencode[codon])
print(''.join(aas))
