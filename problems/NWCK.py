"""Distances in Trees.

Given: A collection of n trees (n ≤ 40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is
followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.
"""

import os

from utils import read_newick


def get_paths(tree):
    paths = []
    stack = [(tree, [tree])]
    while stack:
        node, path = stack.pop()
        paths.append(path)
        for child in node.children:
            child_path = path.copy()
            child_path.append(child)
            stack.append((child, child_path))
    return paths


data = """\
(cat)dog;
dog cat

(dog,cat);
dog cat
"""

lines = data.rstrip('\n').split('\n')
i = 0
records = []
while i < len(lines):
    if not lines[i]:
        i += 1
        continue

    data_path = 'NWCK.txt'
    with open(data_path, 'w') as file:
        file.write(lines[i])
    tree = read_newick(data_path)
    os.remove(data_path)

    node_name1, node_name2 = lines[i + 1].split()
    records.append((tree, node_name1, node_name2))
    i += 2

distances = []
for tree, node_name1, node_name2 in records:
    paths = {path[-1].name: path for path in get_paths(tree) if path[-1].name}
    path1, path2 = paths[node_name1], paths[node_name2]

    i = 0
    for node1, node2 in zip(path1, path2):
        if node1 is not node2:
            break
        i += 1
    length1, length2 = len(path1[i:]), len(path2[i:])
    distances.append(length1 + length2)

print(' '.join([str(d) for d in distances]))
