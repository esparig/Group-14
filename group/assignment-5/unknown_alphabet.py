"""Given a lexicon of all words in lexicographic order of a fictional Language
find the alphabet of that Language
"""
from typing import List, DefaultDict, Set
from _collections import defaultdict

class Trie:
    """Lexicon: collections of words stored as a Trie.
    """
    def __init__(self, char: str, ends: bool, children: List['Trie']) -> None:
        self.chr = char
        self.ends = ends
        self.children = children

def create_lexicon(words: List[str]) -> Trie:
    """Initialize a lexicon from a list of words
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
    """Traverse the trie getting the relative order of letters:
    a node of the trie contains its children in the given lexicographic order
    """
    if len(node.children) > 0:
        yield [n.chr for n in node.children]
    for elem in node.children:
        yield from get_precedence_rule(prefix+elem.chr, elem)

def topological_sort(adjacency_list: DefaultDict[str, List[str]], vertices: Set[str]) -> List[str]:
    """Topological sort of a graph using the Khan algorithm.
    Inputs:
    a graph as an adjacency list
    Returns:
    a list containing the topological sort of our graph
    """
    in_degree = {}
    for v, adjacents in [(vertex, adjacency_list[vertex]) for vertex in vertices]:
        in_degree.setdefault(v, 0)
        for adj in adjacents:
            in_degree[adj] = in_degree.get(adj, 0) + 1
            
    queue = {v for v, count in in_degree.items() if count == 0}

    result = []
    
    while queue:
        v = queue.pop()
        result.append(v)
        
        for adjacent in adjacency_list.get(v, []):
            in_degree[adjacent] -= 1
            
            if in_degree[adjacent] == 0:
                queue.add(adjacent)
    
    if len(result) != len(in_degree):
        return None
    else:
        return result
               
def get_alphabet(lexicon: Trie) -> List[str]:
    """Obtain the alphabet in lexicographic order of a fictional language
    - Creates the graph as an adjacency list
    - Calls the topological sort function
    """
    adjacency_list = defaultdict(list)
    vertices = set()
    for letters in get_precedence_rule("", lexicon):
        for i, letter in enumerate(letters):
            vertices.add(letter)
            if i < len(letters) - 1:
                adjacency_list[letter].append(letters[i+1])
    return topological_sort(adjacency_list, vertices)
