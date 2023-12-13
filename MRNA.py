"""Inferring mRNA from Protein.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
(Don't neglect the importance of the stop codon in protein translation.)
"""

seq = 'MA'

gencode = {}
with open('constants/codons.txt') as file:
    for line in file:
        keyvals = line.rstrip('\n').split('\t')
        for keyval in keyvals:
            codon, aa = keyval.split()
            gencode[aa] = gencode.get(aa, 0) + 1

count = 1
for sym in seq + '*':  # Append stop codon
    count = (count * gencode[sym]) % 1E6
print(count)
