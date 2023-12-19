"""Finding the Longest Multiple Repeat

Given: A DNA string s (of length at most 20 kbp) with $ appended, a positive integer k, and a list of edges defining the
suffix tree of s. Each edge is represented by four components:

1. the label of its parent node in T(s);
2. the label of its child node in T(s);
3. the location of the substring t of s∗ assigned to the edge; and
4. the length of t.

Return: The longest substring of s that occurs at least k times in s. (If multiple solutions exist, you may return any
single solution.)
"""

from utils.newick import TreeNode

data = """\
CATACATAC$
2
node1 node2 1 1
node1 node7 2 1
node1 node14 3 3
node1 node17 10 1
node2 node3 2 4
node2 node6 10 1
node3 node4 6 5
node3 node5 10 1
node7 node8 3 3
node7 node11 5 1
node8 node9 6 5
node8 node10 10 1
node11 node12 6 5
node11 node13 10 1
node14 node15 6 5
node14 node16 10 1
"""

lines = data.rstrip('\n').split('\n')

s = lines[0]
k = int(lines[1])
edges = []
for line in lines[2:]:
    nameA, nameB, index, length = line.split()
    edges.append((nameA, nameB, int(index), int(length)))

names = set()
for nameA, nameB, _, _ in edges:
    names.update([nameA, nameB])

name2node = {name: TreeNode(name=name) for name in names}
for node in name2node.values():
    node.substrings = []
    node.path = ''
for nameA, nameB, index, length in edges:
    nodeA, nodeB = name2node[nameA], name2node[nameB]
    nodeA.children.append(nodeB)
    nodeB.parent = nodeA
    nodeA.substrings.append(s[index-1:index-1+length])

name = list(names)[0]
tree = name2node[name]
while tree.parent is not None:
    tree = tree.parent

# The path from root to a node encodes a substring
# The number of tips of the final node is the number of times that substring appears
# The path with the longest substring associated with a node is whichever concatenation of the edge substring + corresponding child path is longest
# First set all paths to empty strings
# If child path is not empty, then must have sufficient number of tips
#     Concatenate edge substring and path to get candidate path
# Otherwise if number of tips is above minimum
#     It must be the lowest node that this is true (otherwise the child path would not be empty)
#     The candidate path is the edge substring (because going any lower would include paths below minimum)
for node in tree.traverse(order='post'):
    paths = []
    for child, substring in zip(node.children, node.substrings):
        if child.path != '':
            paths.append(substring + child.path)
        elif len(list(child.tips())) >= k:
            paths.append(substring)
    if paths:
        node.path = max(paths, key=len)

print(tree.path)
