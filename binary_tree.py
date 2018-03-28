#!/usr/bin/env python


class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None


def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
        print(node.value)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data)
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data)
    return node


def isPresent(root, val):
    node = root
    if root is None:
        return 0
    if val == root.value:
        return 1
    elif val < root.value:
        return isPresent(root.left, val)
    elif val > root.value:
        return isPresent(root.right, val)

    if node.left is None and node.right is None:
        return 0


_a = None
_a_size = int(input())
_a_i = 0
_root = None
while _a_i < _a_size:
    _a_item = int(input())
    _a = _insert_node_into_binarysearchtree(_a, _a_item)
    if _a_i == 0:
        _root = _a
    _a_i += 1

q = int(input())
i = 0

while i < q:
    _b = int(input())
    _result = isPresent(_root, _b)
    print(_result)
    i += 1
