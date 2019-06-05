class BinaryTree:
    """Binary tree object. Assumes that there are no specific requirements
    for it to be a binary *search* tree or have any other fancy properties.
    Each single node can be seen as a subtree of its parent, if such exists.
    """

    def __init__(self, key):
        """Creates a new node which is the root of the current tree.

        :param key: the key held by each node used to identify it.
        """
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        """Prints out a textual representation of a BT node, along with
        its direct children.

        :return: string with node contents.
        """
        left = None if self.left is None else self.left.key
        right = None if self.right is None else self.right.key

        return '(Key: {}, Left child: {}, Right child: {})'.format(self.key, left, right)

    def depth_first_traversal(self):
        """Does pre-order depth-first traversal of the subtree
        to which the current node is a root. Recursive.
        This is used as helper when finding for a node in the tree,
        or when searching for ancestors.
        :return: iterable containing BT nodes in depth-first order.
        """
        yield self
        if self.left is not None:
            for left in self.left.depth_first_traversal():
                yield left
        if self.right is not None:
            for right in self.right.depth_first_traversal():
                yield right

    def breadth_first_traversal(self):
        """Does breadth-first traversal of the subtree
        to which the current node is a root. Uses a stack to keep track
        of nodes to visit.
        This is used as helper when adding new nodes to the tree.
        :return: iterable containing BT nodes in breadth-first order.
        """
        to_visit = [self]
        while to_visit:
            current = to_visit.pop(0)
            yield current
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)

    def append_node(self, new_node_key):
        """Creates a new node with the given key and appends it
        at the first "free" space using breadth_first_traversal
        to find a "childless" parent.
        :param new_node_key: key value for new node to be added.
        """
        if new_node_key not in {node.key for node in self.breadth_first_traversal()}:
            for parent in self.breadth_first_traversal():
                if parent.left is None:
                    parent.left = BinaryTree(new_node_key)
                    break
                elif parent.right is None:
                    parent.right = BinaryTree(new_node_key)
                    break

    def find_node(self, search_key):
        """Uses depth-first traversal to find a node with the given key.
        :param search_key: find a node whose key is this value"""
        for node in self.depth_first_traversal():
            if node.key == search_key:
                return node
        return None

    def get_ancestors(self, search_key):
        """Uses depth-first traversal to find ancestors of a node in the tree.
        Recursively returns ancestor nodes from subtrees.
        :param search_key: for a node with this key, find its ancestors
        :return: iterable with ancestor nodes
        """
        if search_key in [node.key for node in self.depth_first_traversal()] and self.key != search_key:
            # Check that the given key is in the current tree; if yes, traverse left and right subtrees
            if self.left is not None and self.left.key != search_key:
                for left in self.left.get_ancestors(search_key):
                    yield left

            if self.right is not None and self.right.key != search_key:
                for right in self.right.get_ancestors(search_key):
                    yield right

            yield self

    def lowest_common_ancestor(self, first_node, second_node):
        """Finds lowest common ancestor of two nodes using a recursive method.
        Assumes that references to nodes will be passed and not keys.
        :param first_node: first node reference to search
        :param second_node: second node reference to search
        :return: node which is lowest common ancestor i.e. is on the path from
        root to both of the nodes and is on as low of a level as possible
        """
        if self.key == first_node.key or self.key == second_node.key:
            # If either of the nodes is the current root, return it.
            # Assumes only the lowest ancestor needs to be returned,
            # so yield is not used here as no need to list all common ancestors
            return self

        # Recursively check subtrees
        left_subtree = self.left.lowest_common_ancestor(first_node, second_node) if self.left is not None else None
        right_subtree = self.right.lowest_common_ancestor(first_node, second_node) if self.right is not None else None

        if left_subtree and right_subtree:
            return self

        return left_subtree or right_subtree


# Example use
def test():
    # Create tree, add some nodes
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


test()
