"""Fixing an Inconsistent Character Set.

Given: An inconsistent character table C on at most 100 taxa.

Return: A submatrix of C′ representing a consistent character table on the same taxa and formed by deleting a single row
of C. (If multiple solutions exist, you may return any one.)

Sample input:
100001
000110
111000
100111

Sample output:
000110
100001
100111
"""

from itertools import combinations, product


def get_splits(characters):
    split0, split1 = set(), set()
    for index, character in enumerate(characters):
        if character == '0':
            split0.add(index)
        else:
            split1.add(index)
    return split0, split1


data = """\
100001
000110
111000
100111
"""

table = data.rstrip('\n').split('\n')

conflicts = []
for characters1, characters2 in combinations(table, 2):
    splits1 = get_splits(characters1)
    splits2 = get_splits(characters2)
    intersections = [sA & sB for sA, sB in product(splits1, splits2)]
    if all(intersections):  # All are nonempty
        conflicts.append((characters1, characters2))

counts = {}
for characters1, characters2 in conflicts:
    counts[characters1] = counts.get(characters1, 0) + 1
    counts[characters2] = counts.get(characters2, 0) + 1

new_table = []
conflict = max(counts, key=lambda x: counts[x])
for character in table:
    if character != conflict:
        new_table.append(character)

for character in new_table:
    print(character)
