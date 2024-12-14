"""Character-Based Phylogeny.

Given: A list of n species (n ≤ 80) and an n-column character table C in which the jth column denotes the jth species.

Return: An unrooted binary tree in Newick format that models C.
"""

from utils.newick import TreeNode


def get_lca(tree, taxa):
    taxa = set(taxa)
    for node in tree.traverse(order='post'):
        if taxa <= set([tip.name for tip in node.tips()]):
            return node
    return None


data = """\
cat dog elephant mouse rabbit rat
011101
001101
001100
"""

lines = data.rstrip('\n').split('\n')
taxa = lines[0].split()
table = lines[1:]

tree = TreeNode(children=[TreeNode(name=taxon) for taxon in taxa])
for characters in table:
    taxa_positive = {taxon for taxon, character in zip(taxa, characters) if character == '1'}
    taxa_negative = {taxon for taxon, character in zip(taxa, characters) if character == '0'}
    for taxa_subset in [taxa_positive, taxa_negative]:
        lca = get_lca(tree, taxa_subset)
        children_subset = []
        children = []
        for child in lca.children:
            if {tip.name for tip in child.tips()} <= taxa_subset:
                children_subset.append(child)
            else:
                children.append(child)
        if not children:  # Check that split introduces new information; may not be necessary for tables w/o repeated characters
            continue
        if lca is tree and len(tree.children) == 3:  # Only split down to three children at root to keep unrooted
            continue
        node_subset = TreeNode(children=children_subset, parent=lca)
        children.append(node_subset)
        lca.children = children

print(tree)
