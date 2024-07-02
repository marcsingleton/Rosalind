"""Inferring Peptide from Full Spectrum.

Given: A list L containing 2n+3 positive real numbers (n ≤ 100). The first number in L is the parent mass of a peptide
P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume
that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every
prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a
protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions
exist, you may output any one.
"""

from math import isclose


def get_match(dx, dy, aa2weight):
    for aa, weight in aa2weight.items():
        if isclose(dx, weight):
            return index, False, aa
        if isclose(dy, weight):
            return index, True, aa
    return None


data = """\
1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091
"""

aa2weight = {}
with open('constants/aa_weights.txt') as file:
    for line in file:
        aa, weight = line.split()
        aa2weight[aa] = float(weight)

weights = [float(weight) for weight in data.split()]
parent = weights[0]

# Find pairs
pairs = []
weight_pool = weights[1:]
while weight_pool:
    index = None
    weight1 = weight_pool.pop()
    for index, weight2 in enumerate(weight_pool):
        if isclose(weight1 + weight2, parent):
            pairs.append({weight1, weight2})
            break
    if index is not None:
        del weight_pool[index]
    else:
        raise RuntimeError


index = min(range(len(pairs)), key=lambda x: min(pairs[x]))
x1, y1 = pairs.pop(index)
if x1 > y1:
    x1, y1 = y1, x1

# Find possible by building out from smallest pre/suffix
peptide = []
while pairs:
    match = None
    for index, (x2, y2) in enumerate(pairs):
        dx = x2 - x1
        dy = y2 - x1
        match = get_match(dx, dy, aa2weight)
        if match is not None:
            break
    if match is not None:
        index, swap, aa = match
        x1, y1 = pairs.pop(index)
        if swap:
            x1, y1 = y1, x1
        peptide.append(aa)
    else:
        raise RuntimeError

print(''.join(peptide))
