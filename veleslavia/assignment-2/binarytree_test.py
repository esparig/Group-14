import unittest

from binarytree import Node


class BinaryTreeChecker(unittest.TestCase):

    def test_get_ancestors(self):
        tree = Node(*(5, (15, 10, 8), (2, 3, 18, 6)))
        self.assertEqual(tree.get_ancestors(2), [5])
        self.assertEqual(tree.get_ancestors(18), [3, 2, 5])

    def test_get_lowest_common(self):
        tree = Node(*(5, (15, 10, 8), (2, 3, 18, 6)))
        self.assertEqual(tree.get_lowest_common_ancestor(2, 3).key, 2)
        self.assertEqual(tree.get_lowest_common_ancestor(8, 18).key, 5)
        self.assertEqual(tree.get_lowest_common_ancestor(3, 15).key, 5)
