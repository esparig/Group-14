"""Unit tests for Assignment 2"""
import unittest

from binary_tree import create_tree_from_list, tree_as_in_order_list, get_node, get_ancestors


class TestAnagrams(unittest.TestCase):
    """Unit Test Class for Binary Tree"""

    def test_tree_creation(self):
        """Test creation of a tree from a list"""
        tree = create_tree_from_list([7, 3, 4, 2, 5, None, 8, 1, 6])
        result = []
        tree_as_in_order_list(tree.head, result)
        self.assertTrue(all([a == b for a, b in zip(result, [1, 2, 6, 3, 5, 7, 4, 8])]))

    def test_find_node(self):
        """Test finding a node in a tree"""
        tree = create_tree_from_list([7, 3, 4, 2, 5, None, 8, 1, 6])
        node = get_node(tree, 6)
        self.assertEqual(node.data, 6)

    def test_find_ancestors(self):
        """Test finding a node in a tree"""
        tree = create_tree_from_list([7, 3, 4, 2, 5, None, 8, 1, 6])
        result = get_ancestors(tree, 6)
        self.assertTrue(all([a == b for a, b in zip(result, [6, 2, 3, 7])]))