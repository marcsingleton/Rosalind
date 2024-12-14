"""Enumerating Unrooted Binary Trees.

Given: A collection of species names representing n taxa.

Return: A list containing all unrooted binary trees whose leaves are these n taxa. Trees should be given in Newick
format, with one tree on each line; the order of the trees is unimportant.
"""

from utils.newick import TreeNode

data = 'Burhinus_constricticollis Haliaetus_regius Pelecanus_grupus Phyllopneuste_leucorodia Rosalia_eburnea Thecla_taxus'

taxa = data.split()

trees = [TreeNode(children=[TreeNode(name=taxon) for taxon in taxa[:3]])]
for taxon in taxa[3:]:
    new_trees = []
    for tree in trees:
        for node_index, node in enumerate(tree.traverse()):
            for child_index, child in enumerate(node.children):
                copy_tree = tree.copy()
                copy_node = list(copy_tree.traverse())[node_index]
                copy_child = copy_node.children.pop(child_index)
                new_child = TreeNode(children=[copy_child, TreeNode(name=taxon)], parent=copy_node)
                copy_node.children.append(new_child)
                new_trees.append(copy_tree)
    trees = new_trees

for tree in trees:
    print(tree)
