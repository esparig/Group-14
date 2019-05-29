"""
Assignment 2: Ancestors.
"""
from typing import List


class BinaryTreeNode:
    """
    Class Binary Tree Node.
    """

    def __init__(self, data: int = None, parent: 'BinaryTreeNode' = None,
                 left: 'BinaryTreeNode' = None, right: 'BinaryTreeNode' = None) -> None:
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def insert_node(self, parent: 'BinaryTreeNode', key: int, is_left: bool) -> None:
        """
        Insert node as left child.
        """
        if is_left:
            self.left = BinaryTreeNode(data=key, parent=parent)
        else:
            self.right = BinaryTreeNode(data=key, parent=parent)

    def print_node(self) -> None:
        """
        Print node info.
        """
        if self.parent:
            parent_data = self.parent.data
        else:
            parent_data = None

        if self.left:
            left_data = self.left.data
        else:
            left_data = None

        if self.right:
            right_data = self.right.data
        else:
            right_data = None

        print('Data: {}, Parent: {}, Left: {}, Right: {}'.format(self.data, parent_data,
                                                                 left_data, right_data))


class BinaryTree:
    """
    Class Binary Tree.
    """

    def __init__(self, head: BinaryTreeNode = None) -> None:
        self.head = head


def tree_as_in_order_list(tree: BinaryTreeNode, result: List[int]) -> None:
    """
    Print a tree in order from its head.
    """
    if tree is not None:
        tree_as_in_order_list(tree.left, result)
        result.append(tree.data)
        tree_as_in_order_list(tree.right, result)


def create_tree_from_list_helper(values: List[int], root: BinaryTreeNode, parent: BinaryTreeNode,
                                 i: int, length: int) -> BinaryTreeNode:
    """
    Helper function to create a tree from a list of values.
    """
    if i < length:
        if values[i] is not None:
            root = BinaryTreeNode(data=values[i], parent=parent)
            root.left = create_tree_from_list_helper(values, root.left, root, 2 * i + 1, length)
            root.right = create_tree_from_list_helper(values, root.right, root, 2 * i + 2, length)

    return root


def create_tree_from_list(values: List[int]) -> BinaryTree:
    """
    Create a tree from a list of values. None value means that there is not a node in that position.
    """
    return BinaryTree(head=create_tree_from_list_helper(values, None, None, 0, len(values)))


def get_node_helper(node: BinaryTreeNode, key: int) -> BinaryTreeNode:
    """
    Helper function to find a node.
    """
    if node.data == key:
        return node
    if node.left:
        found = get_node_helper(node.left, key)
        if found:
            return found
    if node.right:
        found = get_node_helper(node.right, key)
        if found:
            return found


def get_node(tree: BinaryTree, key: int) -> BinaryTreeNode:
    """
    Find a node from the head of a tree.
    """
    return get_node_helper(tree.head, key)


def get_ancestors(tree: BinaryTree, key: int) -> List[int]:
    """
    Find the ancestors of a node.
    """
    ancestors = []
    node = get_node_helper(tree.head, key)
    while not node.parent:
        ancestors.append(node) # the node itself is an ancestor
        node = node.parent
    return ancestors
