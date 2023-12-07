"""Comparing Spectra with the Spectral Convolution.

Given: Two multisets of positive real numbers S1 and S2. The size of each multiset is at most 200.

Return: The largest multiplicity of S1⊖S2, as well as the absolute value of the number x maximizing (S1⊖S2)(x) (you may
return any such value if multiple solutions exist).
"""

from itertools import product


def make_multiset(values):
    multiset = {}
    for value in values:
        multiset[value] = 1 + multiset.get(value, 0)
    return multiset


data = """\
186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544
101.04768 158.06914 202.09536 318.09979 419.14747 463.17369
"""

line1, line2 = data.rstrip().split('\n')
values1 = [float(value) for value in line1.split()]
values2 = [float(value) for value in line2.split()]

diffs = []
for value1, value2 in product(values1, values2):
    diff = round(value1 - value2, 5)
    diffs.append(diff)
mset = make_multiset(diffs)

value, count = max(mset.items(), key=lambda x: x[1])
print(count)
print(abs(value))
