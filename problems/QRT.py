"""Quartets.

Given: A partial character table C.

Return: The collection of all quartets that can be inferred from the splits corresponding to the underlying characters
of C.

Sample input:
cat dog elephant ostrich mouse rabbit robot
01xxx00
x11xx00
111x00x

Sample output:
{elephant, dog} {rabbit, robot}
{cat, dog} {mouse, rabbit}
{mouse, rabbit} {cat, elephant}
{dog, elephant} {mouse, rabbit}
"""

from itertools import combinations, product

data = """\
cat dog elephant ostrich mouse rabbit robot
01xxx00
x11xx00
111x00x
"""

lines = data.rstrip('\n').split('\n')
taxa_order = lines[0].split()
table = lines[1:]

quartets = set()
for characters in table:
    c0, c1 = [], []
    for taxon, character in zip(taxa_order, characters):
        if character == '0':
            c0.append(taxon)
        elif character == '1':
            c1.append(taxon)
    pairs0 = combinations(c0, 2)
    pairs1 = combinations(c1, 2)
    for pair0, pair1 in product(pairs0, pairs1):
        quartets.add(frozenset((frozenset(pair0), frozenset(pair1))))

for quartet in quartets:
    pair0, pair1 = tuple(quartet)
    string0 = '{%s, %s}' % tuple(pair0)
    string1 = '{%s, %s}' % tuple(pair1)
    print(string0, string1)
