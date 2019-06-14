from typing import List, Tuple, Callable


class Lexicon:

    def __init__(self, vocabulary: List[str]) -> None:
        self.vocabulary = vocabulary

    def is_word(self, word: str) -> bool:
        return word in self.vocabulary

    def is_prefix(self, prefix: str) -> bool:
        """ Returns True if the given prefix is a prefix of at least one word in the lexicon
        """
        return any(prefix == word[:len(prefix)] for word in self.vocabulary)


class Grid:
    incident_shifts = ((-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1))

    def __init__(self, letters: List[List[str]]) -> None:
        self.data = letters
        self.is_visited = [[False]*len(self.data[i]) for i in range(len(self.data))]

    def is_valid_to_visit(self, i: int, j: int) -> bool:
        if 0 <= i <= len(self.data) - 1:
            if 0 <= j <= len(self.data[i]) - 1:
                return not self.is_visited[i][j]

    def incident(self, i: int, j: int) -> Tuple[int, int]:
        for (shift_i, shift_j) in self.incident_shifts:
            if self.is_valid_to_visit(i + shift_i, j + shift_j):
                yield i + shift_i, j + shift_j

    def traverse_from(self, i: int, j: int, prefix: str = '', continue_traverse: Callable[[str], bool] = None):
        self.is_visited[i][j] = True
        prefix += self.data[i][j]
        if continue_traverse(prefix):
            yield prefix
            for (incident_i, incident_j) in self.incident(i, j):
                yield from self.traverse_from(incident_i, incident_j, prefix=prefix, continue_traverse=continue_traverse)
                self.is_visited[incident_i][incident_j] = False

    def traverse(self, continue_traverse: Callable[[str], bool] = None):
        for start_row in range(len(self.data)):
            for start_col in range(len(self.data[start_row])):
                self.is_visited = [[False] * len(self.data[i]) for i in range(len(self.data))]
                yield from self.traverse_from(start_row, start_col,
                                              prefix='', continue_traverse=continue_traverse)
