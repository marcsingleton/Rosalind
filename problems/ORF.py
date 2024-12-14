"""Open Reading Frames.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any
order.
"""

from utils import read_fasta, reverse_complement


def get_ORFs(seq):
    i0 = None
    ORFs = []
    for i in range(len(seq) - 1, -1, -1):
        aa = seq[i]
        if aa == '*':
            i0 = i
        elif aa == 'M' and i0 is not None:
            ORFs.append(seq[i:i0])
    return ORFs


def translate(seq, gencode):
    aas = []
    for i in range(0, len(seq) - 3, 3):
        codon = seq[i : i + 3]
        aas.append(gencode[codon])
    return ''.join(aas)


def to_RNA(seq):
    return seq.replace('T', 'U')


data = """\
>Rosalind_0588
AAGGTTGCTGTAGCCGCTTAGCGAATATGTCTGTCTTCAGGAATGGAGGCATGTTCGCGT
GACGAAAATCAAACGCGGTTCACCTAAACTCAGCCTTGGTTCGAATCGAGGAGGTGCCGT
GGTGAAATCGTTGTAGCCGTCCCTTCCCAAAATGCGGTAGTGCAGGGGTAGCTACTTGGT
ATATTAGCAAGTATAAACAAGAGGAGACGTCTTGATCACTTATTAACTTCATACCTTTTG
AGATTATACGTAACTCGATTTTCCACCAGCGTGTGAGACGCTCGCCGATCACGCTCGGGC
ACTCTTCCATGCGCCTAGTGGGACTGATGGGCGAGTAGGAAGCAACTGTTGGAAGTGGGC
GTTAGACTCCTCGCCTGTGTACTTCAACCAGAGCTTGGACAGCAGGCTCAGCCAAGTGGG
GACGCCCCAACCGGGGGCAGGCACTCGGACAATGTGAATGAGGCTTCGGGCCCCACAGTT
TCCATAGCTATGGAAACTGTGGGGCCCGAAGCCTCATTCACATATAAGAAGCCGCACTGA
TGTAACCTATGACAATGTAAGTTCTAAAGCTCTAACCCGCGTGGCATGTAAGCTACTCAG
GCCGCGAACGAGCCTGTCGGCGAGAAAAGACTTACTTGCATGATGTGCAGAGCGATTGGG
ACTATAGTTTGCAGGGCCATAGGTTAACAACCTAGAAACCCCCACCCTAGTCCTCATCAG
CAACTAACCCAGTGACCTGATGCCCCTTCTCCTCCACCCTTTTAGATCTCCTCACCCGGG
ATATACTCGCTTGCTATTTTGCCAGGGCTGCTGGGCTCCATTGAATTGTTCAGACGGAAC
CCGATTTGCGCGTTGTTCAAGCGTTCTTGCGAGAGAACCTCCTGTACCGGCTCAGTGGAA
AGTCTGAATTGGCCGTCAAGCGTAAGCCCCATAGGATGCATGCTCCATACGGGGGATCCA
AGGGTAAGGTAGAC
"""

data_path = 'ORF.txt'
with open(data_path, 'w') as file:
    file.write(data)

fasta = list(read_fasta(data_path))
header, seq = fasta[0]

gencode = {}
with open('constants/codons.txt') as file:
    for line in file:
        keyvals = line.rstrip('\n').split('\t')
        for keyval in keyvals:
            codon, aa = keyval.split()
            gencode[codon] = aa

RNA_forward = to_RNA(seq)
RNA_reverse = to_RNA(reverse_complement(seq))
seqs = [
    RNA_forward,
    RNA_forward[1:],
    RNA_forward[2:],
    RNA_reverse,
    RNA_reverse[1:],
    RNA_reverse[2:],
]

ORFs = []
for seq in seqs:
    ORFs.extend(get_ORFs(translate(seq, gencode)))
for ORF in set(ORFs):  # Prompt requires distinct proteins
    print(ORF)
