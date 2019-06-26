from typing import List, Tuple, Callable, Iterable


class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.is_final = False

    def insert(self, word):
        prefix, *suffix = word
        if prefix not in self.children:
            self.children[prefix] = PrefixTreeNode()
        if suffix:
            self.children[prefix].insert(suffix)
        else:
            self.children[prefix].is_final = True

    def __getitem__(self, item):
        prefix, *suffix = item
        if prefix not in self.children:
            return False
        return self.children[prefix][suffix] if suffix else self.children[prefix]


class Lexicon:

    def __init__(self, vocabulary: List[str]) -> None:

        self.prefix_tree = PrefixTreeNode()
        for word in vocabulary:
            self.prefix_tree.insert(word)

    def is_word(self, word: str) -> bool:
        return self.prefix_tree[word].is_final if self.prefix_tree[word] else False

    def is_prefix(self, prefix: str) -> bool:
        """ Returns True if the given prefix is a prefix of at least one word in the lexicon
        """
        return bool(self.prefix_tree[prefix])


class Grid:
    neighbours = ((-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1))

    def __init__(self, letters: List[List[str]]) -> None:
        self.data = letters
        self.is_visited = [[False]*len(self.data[i]) for i in range(len(self.data))]

    def is_valid_to_visit(self, i: int, j: int) -> bool:
        if 0 <= i <= len(self.data) - 1:
            if 0 <= j <= len(self.data[i]) - 1:
                return not self.is_visited[i][j]

    def valid_neighbours(self, i: int, j: int) -> Iterable[Tuple[int, int]]:
        for (shift_i, shift_j) in self.neighbours:
            if self.is_valid_to_visit(i + shift_i, j + shift_j):
                yield i + shift_i, j + shift_j

    def traverse_from(self, i: int, j: int, prefix: str = '', continue_traverse: Callable[[str], bool] = None):
        self.is_visited[i][j] = True
        prefix += self.data[i][j]
        if continue_traverse(prefix):
            yield prefix
            for (incident_i, incident_j) in self.valid_neighbours(i, j):
                yield from self.traverse_from(incident_i, incident_j, prefix, continue_traverse)
                self.is_visited[incident_i][incident_j] = False

    def traverse(self, continue_traverse: Callable[[str], bool] = None) -> Iterable[str]:
        for start_row in range(len(self.data)):
            for start_col in range(len(self.data[start_row])):
                self.is_visited = [[False] * len(self.data[i]) for i in range(len(self.data))]
                yield from self.traverse_from(start_row, start_col, continue_traverse=continue_traverse)
