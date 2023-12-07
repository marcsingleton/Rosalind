"""Locating Restriction Sites.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return
these pairs in any order.
"""

import os

import numpy as np
from utils import read_fasta

data = """\
>Rosalind_9382
ATATACGAGGGAATATTTCTATCGACCTGTATACCCTCTCGACTCCCCAGGAGCCATCCT
ACTCGATGAGAGAAATTAGATCACGGGACATCCTAATTGATATCTTCTTTGTAGAGCATT
GTCTGCTACCTATTTGGACGACGCTACTCGTTTCCCGCCATTTCCGGGAACCAATGAGCC
TCATATTTGACCTATTCTCCGCCCTAACCGGACTCTGTCCAGTATGTTTCAATGTGCCAG
CTATTCCTAGCATTATCCTCTTCCGACGACGTCGTTAGTGTGTTTGTCCTTCAGGCTATC
GAGGACACATCCTCCAGTGAGGGGATTTGAACCTTGTTCTAGCGTCAAGTAGACATTCAC
ACTGAGGGTCACTCAAGATTAAGATTACGGGATTGCCCAGTCTAATATACTCTCCGTCTA
CAGATTCCGGAATAGATGCCCTAACGGAAGGACATGTCCTCCACAGCAGACGATACAACC
TAAACAAGACCGTTCCGCGACTCAGACAGCCTACCCGTCAGCGACATCTATTACGGTCTT
ACTCAGGCAGCTTCACGTGACGACCGGTACGCCCCTATTTTTCTACCGGTTGTGTTGCTA
ACTCCTCTCTCCAACGCCCCCCAAATGGTGGACTAACCCGCGCGTAAGCCCGGCGCCGCT
ATGCAAAAGGTATCGGATGCACTAACCGATGAACACGCTATTCGACGCGGCATGATCGCG
TAGTCCTGGGAATACATTCCTAGCGCAGTGCAGCCTAAACTATCCACTGTATGCCATACC
ACGTCCGAAGGAGAATGTTTCCAGATCTCTGACCAGTGAATATGGCGGAGAACCTGAAGA
GTGCATCGCCAAGCCACTCTCAGACACATGTCTTCGTGTAGGTCCGGCAATAACCGATAC
TAGTATAT
"""

pairs = [('A', 'T'), ('G', 'C')]
complements = {}
for sym1, sym2 in pairs:
    complements[sym1] = sym2
    complements[sym2] = sym1

data_path = 'REVP.txt'
with open(data_path, 'w') as file:
    file.write(data)

fasta = list(read_fasta(data_path))
header, seq = fasta[0]

# Initialize DP array
n = len(seq)
array = np.zeros((n, n), dtype=bool)
for i in range(n-1):
    sym1, sym2 = seq[i], seq[i+1]
    if sym1 == complements[sym2]:
        array[i, i+1] = True

# Fill DP array along diagonals
for delta in range(2, n):
    for j in range(delta, n):
        i = j - delta
        sym1, sym2 = seq[i], seq[j]
        if sym1 == complements[sym2] and array[i+1, j-1]:
            array[i, j] = True

# Iterate over DP array and print results
for i in range(n):
    for j in range(i, n):
        if array[i, j] and 4 <= j - i + 1 <= 12:
            print(i + 1, j - i + 1)

os.remove(data_path)
