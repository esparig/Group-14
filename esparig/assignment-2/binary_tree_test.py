"""Unit tests for Assignment 2"""
import unittest
from typing import List
from binary_tree import BinaryTreeNode, get_ancestors, common_ancestor

class TestBinaryTree(unittest.TestCase):
    """Unit Test Class for Binary Tree.
    """

    def setUp(self):
        def create_tree_from_list(values: List[int], root: BinaryTreeNode, parent: BinaryTreeNode,
                                 i: int, length: int) -> BinaryTreeNode:
            """Helper function to create a tree from a list of values.
            """
            if i < length:
                if values[i] is not None:
                    root = BinaryTreeNode(data=values[i], parent=parent)
                    root.left = create_tree_from_list(values, root.left, root, 2 * i + 1, length)
                    root.right = create_tree_from_list(values, root.right, root, 2 * i + 2, length)

            return root

        self.tree = create_tree_from_list([7, 3, 4, 2, 5, None, 8, 1, 6], None, None, 0, 9)
        self.alt_tree = create_tree_from_list([10, 11, 12], None, None, 0, 3)

    def test_find_existing_node(self):
        """Test finding an existing node in a tree.
        """
        self.assertEqual(self.tree.find_node(6).data, 6)
        self.assertEqual(self.alt_tree.find_node(10).data, 10)

    def test_find_non_existing_node(self):
        """Test finding an non existing node in a tree.
        """
        self.assertRaises(KeyError, self.tree.find_node, 9)

    def test_ancestors(self):
        """Test list of ancestors of a node that contains a given key.
        """
        self.assertEqual(get_ancestors(self.tree, 6), [6, 2, 3, 7])

    def test_existing_common_ancestor(self):
        """Test common ancestor of two nodes of the same tree.
        """
        self.assertEqual(common_ancestor(self.tree.find_node(6), self.tree.find_node(5)).data, 3)
        self.assertEqual(common_ancestor(self.tree.find_node(1), self.tree.find_node(6)).data, 2)
        self.assertEqual(common_ancestor(self.tree.find_node(6), self.tree.find_node(7)).data, 7)

    def test_non_existing_common_ancestor(self):
        """Test common ancestor of two nodes from different trees.
        """
        self.assertRaises(Exception, common_ancestor,
                          self.tree.find_node(6), self.alt_tree.find_node(10))
