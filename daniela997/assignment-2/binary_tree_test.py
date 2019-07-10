import unittest

from binary_tree import BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree("A")
        self.assertEqual(tree.key, "A")
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_dft(self):
        tree = BinaryTree(1, 2, 3, 4)
        list_ = [1, 2, 4, 3]
        self.assertEqual([node.key for node in tree.depth_first_traversal()], list_)

    def test_bft(self):
        tree = BinaryTree(1, 2, 3, 4)
        list_ = [1, 2, 3, 4]
        self.assertEqual([node.key for node in tree.breadth_first_traversal()], list_)

    def test_append(self):
        tree = BinaryTree(1)
        self.assertIsNone(tree.left)
        tree.append_node(2)
        self.assertEqual(tree.left.key, 2)
        tree.append_node(3)
        self.assertEqual(tree.right.key, 3)
        tree.append_node(2)
        list_ = [1, 2, 3]
        self.assertEqual([node.key for node in tree.breadth_first_traversal()], list_)

    def test_find(self):
        tree = BinaryTree("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
        found1 = tree.find_node("K")
        self.assertEqual(found1.key, "K")
        self.assertRaises(KeyError, tree.find_node, "N")

    def test_ancestors(self):
        tree = BinaryTree("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
        list_ = ["E", "B", "A"]
        self.assertEqual([node.key for node in tree.get_ancestors("K")], list_)
        self.assertEqual(len([node.key for node in tree.get_ancestors("A")]), 0)
        self.assertEqual(len([node.key for node in tree.get_ancestors("Q")]), 0)

    def test_lca(self):
        tree = BinaryTree("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
        first_node = tree.find_node("K")
        second_node = tree.find_node("I")
        lca = tree.lowest_common_ancestor(first_node, second_node)
        self.assertEqual(lca.key, "B")


if __name__ == '__main__':
    unittest.main()
