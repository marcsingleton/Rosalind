"""Finding a Spliced Motif."""

import os

from utils import read_fasta

data = """\
>Rosalind_1326
GCCAAACGTCGAAGGAATGGTTTTCAACCAGAGCGGCACGACCGGGTAGTGTGGGCGGCT
AGTACGCATTTCACCATCGCCCAGAGATTCTCGCGATCTCGCCCACTAAGGGAGACGTTC
ATCGTAACGGATAAACCCTTTCTCGGGAACGCCGTCTCAGCATGTGCGACCGGATACACA
TAGAATCCACTCTGGGCTCTTCATGACCCCTCTCTGAATTCCATAACATTTGGAACCGCA
TGGTCCACCAGATGCAAGGTGAGGTACCCCACCGATGGAATAGGAACAGGAGAGCGGACA
GCCCCAACAGTGTAGGATACACGGCCTTAAGGCAATCTATCTACAAGGTTGGGGGGCTGG
CCCCGAGATAATTCACTTCCTTCCCTACAGACAGACCGGACTTCGGGGTATCCCACCGAG
CAACTATAGTCTACATGGTTGGCAGCATCCACCCCCAGCTTCATAACGCAAATACTGGCT
CCGGACTCCATGAAAGACGATAAGGCTTGTCTCTGTACGAAATCGAACGCCTAGATATTA
TCAACACCGTACACTTCAGACCCCCTTCAATTTAATCTTTGTGACCCCGACTCGAATGGA
ATTCACGTCTCGTACTCTCCAAAGCTCGAGAGTTGGTTGGTAGGATCTGTAGCGATGATA
TGGTCGAGGCGATTATAAATTTTCGTGATCGGTGGCGTGTTCGACACTTACAGTTATAGT
GAAGTATTGATGACACATTAGAATAGCACCCTCCTTGAGAGTCGAGAGTCCTACGTTTGG
CGCTCATATGGGCCCTACCGGAGCAGAGTTACC
>Rosalind_0108
ATGCTCACAGACCGTGCCACACTACTCTACCCCGCTCAGTAACTTAGGTGCTTGTTGTTA
GTTCTAGGGT
"""

data_path = 'SSEQ.txt'
with open(data_path, 'w') as file:
    file.write(data)

fasta = list(read_fasta(data_path))
_, seq1 = fasta[0]
_, seq2 = fasta[1]

indices = []
seq2_index = 0
for seq1_index, sym in enumerate(seq1):
    if sym == seq2[seq2_index]:
        indices.append(seq1_index+1)
        seq2_index += 1
    if seq2_index == len(seq2):
        break

print(' '.join(str(index) for index in indices))

os.remove(data_path)
