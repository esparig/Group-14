import unittest

from binary_tree import BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def test_init(self):
        tree = BinaryTree("A")
        self.assertEqual(tree.key, "A")
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_dft(self):
        tree = BinaryTree(1)
        tree.append_node(2)
        tree.append_node(3)
        tree.append_node(4)
        list_ = [1, 2, 4, 3]
        self.assertEqual([node.key for node in tree.depth_first_traversal()], list_)

    def test_bft(self):
        tree = BinaryTree(1)
        tree.append_node(2)
        tree.append_node(3)
        tree.append_node(4)
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
        tree = BinaryTree("A")
        tree.append_node("B")
        tree.append_node("C")
        tree.append_node("D")
        tree.append_node("E")
        tree.append_node("E")
        tree.append_node("F")
        tree.append_node("G")
        tree.append_node("H")
        tree.append_node("I")
        tree.append_node("J")
        tree.append_node("K")
        tree.append_node("L")
        found1 = tree.find_node("K")
        self.assertEqual(found1.key, "K")
        found2 = tree.find_node("N")
        self.assertIsNone(found2)

    def test_ancestors(self):
        tree = BinaryTree("A")
        tree.append_node("B")
        tree.append_node("C")
        tree.append_node("D")
        tree.append_node("E")
        tree.append_node("E")
        tree.append_node("F")
        tree.append_node("G")
        tree.append_node("H")
        tree.append_node("I")
        tree.append_node("J")
        tree.append_node("K")
        tree.append_node("L")
        list_ = ["E", "B", "A"]
        self.assertEqual([node.key for node in tree.get_ancestors("K")], list_)
        self.assertEqual(len([node.key for node in tree.get_ancestors("A")]), 0)
        self.assertEqual(len([node.key for node in tree.get_ancestors("Q")]), 0)

    def test_lca(self):
        tree = BinaryTree("A")
        tree.append_node("B")
        tree.append_node("C")
        tree.append_node("D")
        tree.append_node("E")
        tree.append_node("E")
        tree.append_node("F")
        tree.append_node("G")
        tree.append_node("H")
        tree.append_node("I")
        tree.append_node("J")
        tree.append_node("K")
        tree.append_node("L")
        first_node = tree.find_node("K")
        second_node = tree.find_node("I")
        lca = tree.lowest_common_ancestor(first_node, second_node)
        self.assertEqual(lca.key, "B")


if __name__ == '__main__':
    unittest.main()
