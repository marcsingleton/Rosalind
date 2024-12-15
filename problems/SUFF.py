"""Encoding Suffix Trees.

Given: A DNA string s of length at most 1kbp.

Return: The substrings of s∗ encoding the edges of the suffix tree for s. You may list these substrings in any order.
"""

from utils.tree import TreeNode

data = 'ATAAATG$'

suffixes = []
for i in range(len(data)):
    suffixes.append(data[i:])

tree = TreeNode()
for suffix in suffixes:
    current_node = tree
    for sym in suffix:
        matching_node = None
        for child in current_node.children:
            if sym == child.substring:
                matching_node = child
                break
        if matching_node is None:
            matching_node = TreeNode(parent=current_node)
            matching_node.substring = sym
            current_node.children.append(matching_node)
        current_node = matching_node

for node in list(tree.traverse(order='post', include_self=False)):
    if len(node.children) == 1:
        child = node.children[0]
        child.parent = None
        node.children = child.children
        node.substring = node.substring + child.substring

for node in tree.traverse(include_self=False):
    print(node.substring)
