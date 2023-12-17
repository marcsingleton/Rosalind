"""Utility functions for manipulating Newick files."""

from string import whitespace

escaped_tokens = set('\\')
structure_tokens = set('(),:;')
whitespace_tokens = set(whitespace)


class TreeNode:
    """Simple class for representing nodes on a tree."""
    def __init__(self, name=None, children=None, parent=None, length=None):
        if children is None:
            children = []
        self.name = name
        self.children = children
        self.parent = parent
        self.length = length
        for child in self.children:
            child.parent = self

    def __repr__(self):
        class_name = type(self).__name__
        node_name = self.name if self.name is not None else 'unnamed'
        children_count = len(self.children)
        repr_string = f'<{class_name}, name: {node_name}, children count: {children_count}>'
        return repr_string

    def __str__(self):
        return self.to_newick()

    def traverse(self, include_self=True, order='pre'):
        if order == 'pre':
            return self._preorder(include_self=include_self)
        elif order == 'post':
            return self._postorder(include_self=include_self)
        elif order == 'level':
            return self._levelorder(include_self=include_self)
        else:
            raise ValueError('order is not one of pre, post, or level')

    def _levelorder(self, include_self=True):
        stack = []
        if include_self:
            stack.append(self)
        else:
            stack.extend(self.children)
        while stack:
            current_node = stack.pop(0)
            yield current_node
            stack.extend(current_node.children)

    def _postorder(self, include_self=True):
        stack = []
        if include_self:
            stack.append(self)
        else:
            stack.extend(self.children)
        while stack:
            current_node = stack.pop()
            if stack and current_node is stack[-1]:
                yield stack.pop()
            else:
                stack.extend([current_node, current_node])
                stack.extend(current_node.children[::-1])

    def _preorder(self, include_self=True):
        stack = []
        if include_self:
            stack.append(self)
        else:
            stack.extend(self.children[::-1])
        while stack:
            current_node = stack.pop()
            yield current_node
            stack.extend(current_node.children[::-1])

    def is_root(self):
        return self.parent is None

    def is_tip(self):
        return not bool(self.children)

    def tips(self, include_self=True, order='pre'):
        for node in self.traverse(include_self=include_self, order=order):
            if node.is_tip():
                yield node

    def non_tips(self, include_self=True, order='pre'):
        for node in self.traverse(include_self=include_self, order=order):
            if not node.is_tip():
                yield node

    def to_newick(self):
        nw_strings = []
        for node in self.traverse(order='post'):
            name = node.name if node.name is not None else ''
            length = f':{node.length}' if node.length else ''
            if node.is_tip():
                nw_strings.append(f'{name}{length}')
            else:
                children_newicks = [nw_strings.pop() for _ in node.children]
                nw_string = '(' + ', '.join(children_newicks) + f'){name}{length}'
                nw_strings.append(nw_string)
        nw_string = nw_strings.pop()
        return nw_string + ';'


def read_newick(path):
    """Read Newick file at path and return tree.

    Parameters
    ----------
    path: str
        Path to Newick file

    Returns
    -------
    tree: TreeNode
    """
    with open(path) as file:
        nw_string = file.read().rstrip()
        nw_tokens = tokenize_newick(nw_string)
        tree = parse_newick(nw_tokens)
        return tree


def tokenize_newick(nw_string):
    is_escaped = False
    tokens = []
    buffer = []  # Buffer for label or length

    i = 0
    while i < len(nw_string):
        sym = nw_string[i]
        if not is_escaped and sym in escaped_tokens:
            is_escaped = True
            i += 1
        elif not is_escaped and sym in structure_tokens:
            if buffer:
                tokens.append(''.join(buffer))
                buffer = []
            tokens.append(sym)
            i += 1
        elif not is_escaped and sym in whitespace_tokens:
            if buffer:
                tokens.append(''.join(buffer))
                buffer = []
            i += 1
        else:  # Otherwise sym is part of label or length
            buffer.append(sym)
            is_escaped = False
            i += 1

    return tokens


def parse_newick(nw_tokens):
    current_node = TreeNode()
    current_parent = None

    i = 0
    while i < len(nw_tokens):
        token = nw_tokens[i]
        if token == '(':
            current_parent = current_node
            current_node = TreeNode(parent=current_parent)
            current_parent.children.append(current_node)
            i += 1
        elif token == ')':
            current_node = current_node.parent
            current_parent = current_node.parent
            i += 1
        elif token == ',':
            current_node = TreeNode(parent=current_parent)
            current_parent.children.append(current_node)
            i += 1
        elif token == ':':
            length_token = nw_tokens[i+1]
            current_node.length = float(length_token)
            i += 2
        elif token == ';':
            i += 1
        else:
            current_node.name = token
            i += 1

    return current_node
