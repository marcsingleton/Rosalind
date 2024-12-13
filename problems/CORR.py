"""Error Correction in Reads.

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were
generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:

s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s  is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one
correct read in the dataset (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol
substitution, and you may return the corrections in any order.)
"""

import os

from utils import read_fasta, reverse_complement


def get_hamming(s1, s2):
    d = 0
    for sym1, sym2 in zip(s1, s2):
        d += 0 if sym1 == sym2 else 1
    return d


data = """\
>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC
"""

data_path = 'CORR.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

seqs = [seq for _, seq in fasta]

counts = {}
for seq in seqs:
    rev = reverse_complement(seq)
    counts[seq] = 1 + counts.get(seq, 0)
    counts[rev] = 1 + counts.get(rev, 0)

seqs_correct = []
seqs_error = []
for seq, count in counts.items():
    if count >= 2:
        seqs_correct.append(seq)
    else:
        seqs_error.append(seq)

for seq_error in set(seqs_error) & set(seqs):
    for seq_correct in seqs_correct:
        dH = get_hamming(seq_error, seq_correct)
        if dH == 1:
            print(f'{seq_error}->{seq_correct}')
            break
