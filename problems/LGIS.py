"""Longest Increasing Subsequence.

Given: A positive integer n ≤ 10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample input:
5
5 1 4 2 3

Sample output:
1 2 3
5 4 2
"""


def get_liss(seq):
    array = [(1, None) for _ in range(len(seq))]
    for i in range(len(seq)):
        length_i, index_i = 1, None
        value_i = seq[i]
        for j in range(i):
            length_j, _ = array[j]
            value_j = seq[j]
            if value_i > value_j and length_j + 1 > length_i:
                length_i = length_j + 1
                index_i = j
        array[i] = (length_i, index_i)

    index = max(range(len(seq)), key=lambda x: array[x][0])
    values = []
    while index is not None:
        values.append(seq[index])
        _, index = array[index]

    return list(reversed(values))


n = 5
string = '5 1 4 2 3'

seq = [int(value) for value in string.split()]
liss = get_liss(seq)
print(' '.join([str(value) for value in liss]))

seq = [-int(value) for value in string.split()]
liss = get_liss(seq)
print(' '.join([str(-value) for value in liss]))
