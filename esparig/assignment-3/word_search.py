"""
Assignment 3: Word Search.
"""
from typing import List, Set

class TrieNode:
    """Lexicon: collections of cords stored as a Trie.
    """
    def __init__(self, char: str, ends: bool, next_char: List['TrieNode']) -> None:
        self.chr = char
        self.ends = ends
        self.next = next_char

    def is_word(self, word: str) -> bool:
        """Takes a string and returns whether the string is a word in the lexicon.
        """
        if not word:
            return self.ends

        for elem in self.next:
            if word[0] == elem.chr:
                return elem.is_word(word[1:])

    def is_prefix(self, prefix: str) -> bool:
        """Takes a string and returns whether the string is a prefix of a word in the lexicon.
        """
        if not prefix:
            if self.next:
                return True
            return False

        for elem in self.next:
            if prefix[0] == elem.chr:
                return elem.is_prefix(prefix[1:])
            
def create_lexicon(words: List[str]) -> TrieNode:
    """Initialize a lexicon.
    """
    lexicon = TrieNode(None, False, [])
    for word in words:
        node = lexicon
        for char in word:
            if not node.next:
                elem = TrieNode(char, False, [])
                node.next.append(elem)
            else:
                found = False
                for elem in node.next:
                    if char == elem.chr:
                        found = True
                        break
                if not found:
                    elem = TrieNode(char, False, [])
                    node.next.append(elem)
            node = elem
        node.ends = True
    return lexicon

def traverse_lexicon(prefix: str, node: TrieNode, words: List[str]) -> List[str]:
    if node.ends:
        words.append(prefix)
    for elem in node.next:
        traverse_lexicon(prefix+elem.chr, elem, words)
        
def words_from_grid(lexicon: TrieNode, grid: List[List[str]], rows: int, cols: int) -> Set[str]:
    """Find the words from the lexicon that can be formed in the grid.
    """
    found_str = set()
    def words_from_grid_helper(current_str: str, i: int, j: int, visited: List[List[bool]]) -> bool:
        """Search and store words using DFS.
        """
        if lexicon.is_prefix(current_str):
            for pos in [0, 1, 2, 3, 5, 6, 7, 8]:
                pos_i, pos_j = pos//cols + i - 1, pos%cols + j - 1
                if pos_i >= 0 and pos_j >= 0 and pos_i < rows and pos_j < cols:
                    if not visited[pos_i][pos_j]:
                        visited[pos_i][pos_j] = True
                        words_from_grid_helper(current_str+grid[pos_i][pos_j],
                                               pos_i, pos_j, visited)
                        visited = [[False]*cols for _ in range(rows)]
        if lexicon.is_word(current_str):
            found_str.add(current_str)

    for i in range(rows):
        for j in range(cols):
            current_str = grid[i][j]
            words_from_grid_helper(current_str, i, j, [[False]*cols for _ in range(rows)])
    return found_str
