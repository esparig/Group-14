from collections import deque


class BinaryTree:
    """Binary tree object. Assumes that there are no specific requirements
    for it to be a binary *search* tree or have any other fancy properties.
    Each single node can be seen as a subtree of its parent, if such exists.
    """

    def __init__(self, *args):
        """Creates a new node which is the root of the current tree.

        :param args: the keys held by each node used to identify it.
        """
        self.key = args[0]
        self.left = None
        self.right = None

        # If more than 1 key is provided create those nodes and attach them
        for arg in args[1:]:
            self.append_node(arg)

    def __repr__(self):
        """Prints out a textual representation of a BT node, along with
        its direct children.

        :return: string with node contents.
        """
        left = None if self.left is None else self.left.key
        right = None if self.right is None else self.right.key

        return f'(Key: {self.key}, Left child: {left}, Right child: {right})'

    def __iter__(self):
        """
        Map DFT to iter class method.
        :return: iterator over the BT nodes
        """
        return self.depth_first_traversal()

    def depth_first_traversal(self):
        """Does pre-order depth-first traversal of the subtree
        to which the current node is a root. Recursive.
        This is used as helper when finding for a node in the tree,
        or when searching for ancestors.
        :return: iterator containing BT nodes in depth-first order.
        """
        yield self
        if self.left is not None:
            yield from self.left.depth_first_traversal()
        if self.right is not None:
            yield from self.right.depth_first_traversal()

    def breadth_first_traversal(self):
        """Does breadth-first traversal of the subtree
        to which the current node is a root. Uses a stack to keep track
        of nodes to visit.
        This is used as helper when adding new nodes to the tree.
        :return: iterator containing BT nodes in breadth-first order.
        """
        to_visit = deque([self])
        # Use doubly linked list to pop 0th element in constant time
        while to_visit:
            current = to_visit.popleft()
            yield current
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)

    def append_node(self, new_node_key):
        """Creates a new node with the given key and appends it
        at the first "free" space using breadth_first_traversal
        to find a "childless" parent. Assumes node keys are unique.
        :param new_node_key: key value for new node to be added.
        """
        if new_node_key not in {node.key for node in self}:
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
        for node in self:
            if node.key == search_key:
                return node
        raise KeyError("There exists no node with this key.")

    def get_ancestors(self, search_key):
        """Uses depth-first traversal to find ancestors of a node in the tree.
        Recursively returns ancestor nodes from subtrees.
        :param search_key: for a node with this key, find its ancestors
        :return: iterator with ancestor nodes
        """
        if search_key in [node.key for node in self] and self.key != search_key:
            # Check that the given key is in the current tree; if yes, traverse left and right subtrees
            if self.left is not None and self.left.key != search_key:
                yield from self.left.get_ancestors(search_key)

            if self.right is not None and self.right.key != search_key:
                yield from self.right.get_ancestors(search_key)

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
