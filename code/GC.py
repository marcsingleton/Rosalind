"""Computing GC Content.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error
below.
"""

import os

from utils import read_fasta

data = """\
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

data_path = 'GC.txt'
with open(data_path, 'w') as file:
    file.write(data)
fasta = list(read_fasta(data_path))
os.remove(data_path)

gcs = []
for header, seq in fasta:
    g = seq.count('G')
    c = seq.count('C')
    gc = g + c
    gcs.append((header, 100 * gc / len(seq)))

max_id, max_gc = max(gcs, key=lambda x: x[1])
print(max_id)
print(max_gc)
