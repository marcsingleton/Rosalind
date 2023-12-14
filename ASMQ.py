"""Assessing Assembly Quality with N50 and N75.

Given: A collection of at most 1000 DNA strings (whose combined length does not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.
"""

from itertools import groupby


def get_N_statistic(seqs, N):
    lengths = sorted([len(seq) for seq in seqs], key=lambda x: -x)
    total_length = sum(lengths)

    running_sum = 0
    for key, group in groupby(lengths):
        running_sum += sum(group)
        if running_sum >= N * total_length:
            return key
    return None


data = """\
GATTACA
TACTACTAC
ATTGAT
GAAGA
"""

seqs = data.rstrip('\n').split('\n')

N50 = get_N_statistic(seqs, 0.5)
N75 = get_N_statistic(seqs, 0.75)

print(N50, N75)
