

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def __repr__(self):
        self.traverse(self.root)

    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(node.key)
            self.traverse(node.right)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def get_ancestors(self, key):
        return self._get_ancestors_recursive(self.root, key)

    def get_lowest_common_ancestor(self, key1, key2):
        """ Returns common ancestor of key1 and key2
        """
        return self._get_lowest_common_ancestor(self.root, key1, key2)

    def _insert_recursive(self, node, key):
        if node is None:
            node = Node(key)
            return node
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if node.key < key:
            return self._search_recursive(node.right, key)
        return self._search_recursive(node.left, key)

    def _get_ancestors_recursive(self, node, key):
        # TODO clean branches
        if (node.left is None) and (node.right is None):
            return list()
        if node.left is not None:
            if key == node.left.key:
                return list([node.key])
            left_ancestors = self._get_ancestors_recursive(node.left, key)
            if left_ancestors:
                left_ancestors.append(node.key)
                return left_ancestors
        if node.right is not None:
            if key == node.right.key:
                return list([node.key])
            right_ancestors = self._get_ancestors_recursive(node.right, key)
            if right_ancestors:
                right_ancestors.append(node.key)
                return right_ancestors

    def _get_lowest_common_ancestor(self, node, key1, key2):
        if node is None:
            return node
        if node.key == key1 or node.key == key2:
            return node
        left_lowest_common = self._get_lowest_common_ancestor(node.left, key1, key2)
        right_lowest_common = self._get_lowest_common_ancestor(node.right, key1, key2)
        if left_lowest_common and right_lowest_common:
            return node

        return left_lowest_common if left_lowest_common is not None else right_lowest_common
