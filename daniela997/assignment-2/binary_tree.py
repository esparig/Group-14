class BinaryTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.key
        right = None if self.right is None else self.right.key

        return '(Key:{}, Left child:{}, Right child:{})'.format(self.key, left, right)

    def depth_first_traversal(self):
        yield self
        if self.left is not None:
            for left in self.left.depth_first_traversal():
                yield left
        if self.right is not None:
            for right in self.right.depth_first_traversal():
                yield right

    def breadth_first_traversal(self):
        to_visit = [self]
        while to_visit:
            current = to_visit.pop(0)
            yield current
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)

    def append_node(self, new_node_key):
        if new_node_key not in {node.key for node in self.breadth_first_traversal()}:
            for parent in self.breadth_first_traversal():
                if parent.left is None:
                    parent.left = BinaryTree(new_node_key)
                    break
                elif parent.right is None:
                    parent.right = BinaryTree(new_node_key)
                    break

    def find_node(self, search_key):
        for node in self.depth_first_traversal():
            if node.key == search_key:
                return node
        return None


def test():
    tree = BinaryTree("A")
    tree.append_node("B")
    tree.append_node("C")
    tree.append_node("D")
    tree.append_node("E")
    tree.append_node("E")

    print([node.key for node in tree.breadth_first_traversal()])
    print([node.key for node in tree.depth_first_traversal()])

    print(tree.find_node("F"))
    print(tree.find_node("B"))



test()
