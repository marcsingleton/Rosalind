"""Creating a Character Table.

Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. The columns of the character table should
encode the taxa ordered lexicographically; the rows of the character table may be given in any order. Also, for any
given character, the particular subset of taxa to which 1s are assigned is arbitrary.
"""

import os

from utils import read_newick

data = """\
(dog,((elephant,mouse),robot),cat);
"""

data_path = 'CTBL.txt'
with open(data_path, 'w') as file:
    file.write(data)

tree = read_newick(data_path)

taxa_order = sorted([tip.name for tip in tree.tips()])
taxa_set = set(taxa_order)
table = []
for node in tree.traverse():
    if node.is_tip():
        continue
    for child in node.children:
        split1 = {tip.name for tip in child.tips()}
        split2 = taxa_set - split1
        if len(split1) == 1 or len(split2) == 1:
            continue
        characters = []
        for taxon in taxa_order:
            if taxon in split1:
                character = 1
            else:
                character = 0
            characters.append(character)
        table.append(characters)

for characters in table:
    print(''.join([str(character) for character in characters]))

os.remove(data_path)
