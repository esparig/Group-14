import unittest

from binarytree import BinaryTree


class BinaryTreeChecker(unittest.TestCase):

    def test_get_ancestors(self):
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(15)
        tree.insert(10)
        tree.insert(8)
        tree.insert(2)
        tree.insert(3)
        tree.insert(18)
        tree.insert(6)
        self.assertEqual(tree.get_ancestors(2), [5])
        self.assertEqual(tree.get_ancestors(8), [10, 15, 5])

    def test_get_lowest_common(self):
        tree = BinaryTree()
        tree.insert(5)
        tree.insert(15)
        tree.insert(10)
        tree.insert(8)
        tree.insert(2)
        tree.insert(3)
        tree.insert(18)
        tree.insert(6)
        self.assertEqual(tree.get_lowest_common_ancestor(2, 3).key, 2)
        self.assertEqual(tree.get_lowest_common_ancestor(8, 18).key, 15)
        self.assertEqual(tree.get_lowest_common_ancestor(3, 15).key, 5)
