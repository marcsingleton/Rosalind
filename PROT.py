"""Translating RNA into Protein."""

seq = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

gencode = {}
with open('constants/codons.txt') as file:
    for line in file:
        keyvals = line.rstrip().split('\t')
        for keyval in keyvals:
            codon, aa = keyval.split()
            gencode[codon] = aa

aas = []
for i in range(0, len(seq) - 3, 3):
    codon = seq[i:i+3]
    aas.append(gencode[codon])
print(''.join(aas))
