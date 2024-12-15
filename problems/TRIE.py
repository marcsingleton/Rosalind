"""Introduction to Pattern Matching.

Given: A list of at most 100 DNA strings of length at most 100 bp, none of which is a prefix of another.

Return: The adjacency list corresponding to the trie T for these patterns, in the following format. If T has n nodes,
first label the root with 1 and then label the remaining nodes with the integers 2 through n in any order you like. Each
edge of the adjacency list of T will be encoded by a triple containing the integer representing the edge's parent node,
followed by the integer representing the edge's child node, and finally the symbol labeling the edge.

Sample input:
ATAGA
ATC
GAT

Sample output:
1 2 A
2 3 T
3 4 A
4 5 G
5 6 A
3 7 C
1 8 G
8 9 A
9 10 T
"""

from utils.tree import TreeNode

data = """\
ATAGA
ATC
GAT
"""

seqs = data.split()

tree = TreeNode(name=1)
node_count = 2
for seq in seqs:
    current_node = tree
    for sym in seq:
        matching_node = None
        for child in current_node.children:
            if sym == child.substring:
                matching_node = child
                break
        if matching_node is None:
            matching_node = TreeNode(name=node_count, parent=current_node)
            matching_node.substring = sym
            current_node.children.append(matching_node)
            node_count += 1
        current_node = matching_node

for node in tree.traverse():
    for child in node.children:
        print(node.name, child.name, child.substring)
