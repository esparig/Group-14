

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = Node(*(left[0], left[1:len(left)//2+1], left[len(left)//2+1:])) if left else None
        self.right = Node(*(right[0], right[1:len(right)//2+1], right[len(right)//2+1:])) if right else None

    def __repr__(self):
        return ' '.join(str(key) for key in self)

    def __iter__(self):
        yield self.key
        if self.left:
            yield from self.left
        if self.right:
            yield from self.right

    def get_ancestors(self, key):
        return [ancestor for ancestor in self._ancestors(key)]

    def _ancestors(self, key):
        if key in self and self.key != key:
            if self.left and self.left.key != key:
                yield from self.left.get_ancestors(key)
            if self.right and self.right.key != key:
                yield from self.right.get_ancestors(key)
            yield self.key

    def get_lowest_common_ancestor(self, key1, key2):

        if key1 in self and key2 in self:
            if self.key == key1 or self.key == key2:
                return self
            if (key1 in self.left and key2 in self.right) or (key2 in self.left and key1 in self.right):
                return self
            left_lowest_common = self.left.get_lowest_common_ancestor(key1, key2) if self.left else None
            right_lowest_common = self.right.get_lowest_common_ancestor(key1, key2) if self.right else None
            return left_lowest_common if left_lowest_common is not None else right_lowest_common
