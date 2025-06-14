"""Finding a Shared Motif.

Given: A collection of k (k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample input:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample output:
AC
"""

from io import StringIO

from utils import parse_fasta


def get_substrings(s):
    substrings = []
    for j in range(1, len(s) + 1):
        for i in range(j):
            substrings.append(s[i:j])
    return substrings


data = """\
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

fasta = list(parse_fasta(StringIO(data)))

substring_sets = []
for _, seq in fasta:
    substring_sets.append(set(get_substrings(seq)))

common_substrings = set.intersection(*substring_sets)
longest_substring = max(common_substrings, key=len)
print(longest_substring)
