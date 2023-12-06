"""Completing a Tree."""


def get_components(graph):
    search_stack = list(graph)
    if not search_stack:  # Catch empty graph
        return []

    node = search_stack.pop()
    component = [node]
    expand_stack = graph[node]
    visited = {node}

    components = []
    while search_stack or expand_stack:
        while expand_stack:
            node = expand_stack.pop()
            if node not in visited:
                component.append(node)
                expand_stack.extend(graph[node])
                visited.add(node)
        components.append(component)

        while search_stack:
            node = search_stack.pop()
            if node not in visited:
                component = [node]
                expand_stack.extend(graph[node])
                visited.add(node)
                break

    return components


data = """\
10
1 2
2 8
4 10
5 9
6 10
7 9
"""

# Make graph
lines = data.rstrip('\n').split('\n')
n = int(lines[0])
graph = {str(i + 1): [] for i in range(n)}  # Nodes numbered at 1
for line in lines[1:]:
    node1, node2 = line.split()
    graph[node1].append(node2)
    graph[node2].append(node1)

# Calculate number of edges
components = get_components(graph)
print(len(components) - 1)
