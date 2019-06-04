class BinaryTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.key
        right = None if self.right is None else self.right.key

        return '(Key:{}, Left child:{}, Right child:{})'.format(self.key, left, right)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

    def set_left(self, left_key):
        if self.left is None:
            self.left = BinaryTree(left_key)
        else:
            self.left.set_left(left_key)

    def set_right(self, right_key):
        if self.right is None:
            self.right = BinaryTree(right_key)
        else:
            self.right.set_right(right_key)

    def depth_first_traversal(self):
        if self.left is not None:
            for left in self.left.depth_first_traversal():
                yield left
        yield self.key
        if self.right is not None:
            for right in self.right.depth_first_traversal():
                yield right


def test():
    tree = BinaryTree("A")
    tree.set_left("B")
    tree.set_right("C")
    tree.set_left("D")
    print(list(tree.depth_first_traversal()))


test()
