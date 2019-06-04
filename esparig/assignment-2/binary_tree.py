"""
Assignment 2: Ancestors.
"""
from typing import List, Iterator


class BinaryTreeNode:
    """
    Class Binary Tree Node.
    """

    def __init__(self, data: int=None, parent: 'BinaryTreeNode'=None,
                 left: 'BinaryTreeNode'=None, right: 'BinaryTreeNode'=None) -> None:
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def find_node(self, key: int) -> 'BinaryTreeNode':
        """Find a node: given a tree and a key, returns a reference
        to the node conaining the given key.
        """
        if self.data == key:
            return self

        if self.left:
            node_found = self.left.find_node(key)
            if node_found:
                return node_found

        if self.right:
            node_found = self.right.find_node(key)
            if node_found:
                return node_found

        if self.parent:
            return None

        raise KeyError("The key is not in this tree.")

    def ancestors(self) -> Iterator['BinaryTreeNode']:
        """Returns all ancestor of a given node.
        """
        node = self
        while node:
            yield node.data
            node = node.parent

def get_ancestors(tree: BinaryTreeNode, key: int) -> List[int]:
    """Returns a list of all ancestors of a node containing the given key
    in the given tree (including itself) as decribed in the assignment.
    """
    return list(tree.find_node(key).ancestors())

def _len_iterable(iterable: Iterator) -> int:
    """Returns the length of an interator without having to converting to a list.
    """
    return sum(1 for _ in iterable)

def common_ancestor(node1: BinaryTreeNode, node2: BinaryTreeNode) -> BinaryTreeNode:
    """Returns the common ancestor node of two given nodes.
    """
    depth1, depth2 = _len_iterable(node1.ancestors()), _len_iterable(node2.ancestors())
    node_up, node_stay = (node1, node2) if depth1 > depth2 else (node2, node1)
    for _ in range(abs(depth1-depth2)):
        node_up = node_up.parent
    while node_up != node_stay:
        node_up, node_stay = node_up.parent, node_stay.parent
    if node_up:
        return node_up
    raise Exception("The nodes doesn't share a common ancestor.")
