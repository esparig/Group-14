"""Given a lexicon of all words in lexicographil order of a fictional Language
find the alphabet of that Language
"""
from typing import List
from collections import deque
class Trie:
    """Lexicon: collections of words stored as a Trie.
    """
    def __init__(self, char: str, ends: bool, children: List['Trie']) -> None:
        self.chr = char
        self.ends = ends
        self.children = children

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
            if self.children:
                return True
            return False

        for elem in self.children:
            if prefix[0] == elem.chr:
                return elem.is_prefix(prefix[1:])

def create_lexicon(words: List[str]) -> Trie:
    """Initialize a lexicon.
    """
    lexicon = Trie(None, False, [])
    for word in words:
        node = lexicon
        for char in word:
            if not node.children:
                elem = Trie(char, False, [])
                node.children.append(elem)
            else:
                found = False
                for elem in node.children:
                    if char == elem.chr:
                        found = True
                        break
                if not found:
                    elem = Trie(char, False, [])
                    node.children.append(elem)
            node = elem
        node.ends = True
    return lexicon

def get_precedence_rule(prefix: str, node: Trie) -> List[str]:
    if len(node.children) > 1:
        yield [n.chr for n in node.children]
    for elem in node.children:
        get_precedence_rule(prefix+elem.chr, elem)
        
def get_alphabet(lexicon: Trie) -> List[str]:
    
    precedence_graph = {}
    for letters in get_precedence_rule("", lexicon):
        for i, letter in enumerate(letters):
            precedence_graph[letter] = letters[i+1]  if i < len(letters)-1 else None
    print(precedence_graph)

lexicon = create_lexicon(["ART", "RAT", "CAT", "CAR"])
get_alphabet(lexicon)