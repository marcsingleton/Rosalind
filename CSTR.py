"""Creating a Character Table from Genetic Strings.

Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the
strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)
"""

data = """\
ATGCTACC
CGTTTACC
ATTCGACC
AGTCTCCC
CGTCTATC
"""

seqs = data.rstrip('\n').split('\n')

nrow = len(seqs)
ncol = len(seqs[0])

table = []
for j in range(ncol):
    sym_counts = {}
    for seq in seqs:
        sym_counts[seq[j]] = sym_counts.get(seq[j], 0) + 1
    if len(sym_counts) != 2 or min(sym_counts.values()) == 1:
        continue
    characters = []
    sym0 = seqs[0][j]
    for seq in seqs:
        if seq[j] == sym0:
            characters.append(1)
        else:
            characters.append(0)
    table.append(characters)

for characters in table:
    print(''.join([str(character) for character in characters]))
