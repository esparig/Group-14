import sys

from binary_tree import BinaryTree


def main(args):
    # Create tree, add some nodes
    tree = BinaryTree("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")

    # Traverse
    print([node.key for node in tree.breadth_first_traversal()])
    print([node.key for node in tree.depth_first_traversal()])

    # Find nodes
    print(tree.find_node("Z"))
    print(tree.find_node("E"))

    # Find ancestors
    print([node for node in tree.get_ancestors("K")])
    print([node for node in tree.get_ancestors("L")])

    # Find common ancestor
    first_node = tree.find_node("K")
    second_node = tree.find_node("L")
    print(tree.lowest_common_ancestor(first_node, second_node))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
