"""Newick Format with Edge Weights.

Given: A collection of n weighted trees (n ≤ 40) in Newick format, with each tree containing at most 200 nodes; each
tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.

Sample input:
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant

Sample output:
75 136
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
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant
"""

lines = data.rstrip('\n').split('\n')
i = 0
records = []
while i < len(lines):
    if not lines[i]:
        i += 1
        continue

    data_path = 'NKEW.txt'
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
    length1 = sum([node.length for node in path1[i:]])
    length2 = sum([node.length for node in path2[i:]])
    distances.append(length1 + length2)

print(' '.join([str(int(d)) for d in distances]))
