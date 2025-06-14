"""Phylogeny Comparison with Split Distance.

Given: A collection of at most 3,000 species taxa and two unrooted binary trees T1 and T2 on these taxa in Newick
format.

Return: The split distance dsplit(T1,T2).

Sample input:
dog rat elephant mouse cat rabbit
(rat,(dog,cat),(rabbit,(elephant,mouse)));
(rat,(cat,dog),(elephant,(mouse,rabbit)));

Sample output:
2
"""

from utils import TreeNode


def get_splits(tree):
    taxa_set = {tip.name for tip in tree.tips()}
    splits = set()
    for node in tree.traverse():
        for child in node.children:
            s1 = frozenset([tip.name for tip in child.tips()])
            s2 = frozenset(taxa_set - s1)
            if len(s1) == 1 or len(s2) == 1:
                continue
            splits.add(frozenset([s1, s2]))
    return splits


data = """\
dog rat elephant mouse cat rabbit
(rat,(dog,cat),(rabbit,(elephant,mouse)));
(rat,(cat,dog),(elephant,(mouse,rabbit)));
"""

lines = data.rstrip('\n').split('\n')
taxa = lines[0].split()
newick1 = lines[1]
newick2 = lines[2]

tree1 = TreeNode.from_newick(newick1)
tree2 = TreeNode.from_newick(newick2)

splits1 = get_splits(tree1)
splits2 = get_splits(tree2)

print(2 * (len(taxa) - 3) - 2 * len(splits1 & splits2))
