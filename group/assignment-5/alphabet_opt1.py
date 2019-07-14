"""Given a lexicon of all words in lexicographic order of a fictional Language
find the alphabet of that Language
"""
from typing import List, Dict
from itertools import permutations, product

LEXICON = ["ART", "RAT", "CAT", "CAR", "MIK"]


class DisjointSet:

    def __init__(self):
        self.sets = list()

    def __getitem__(self, item):
        return self.sets[item]

    def make_set(self, vertex):
        self.sets.append({vertex: []})

    def union(self, vertex1, vertex2):
        set1 = self.find(vertex1)
        set2 = self.find(vertex2)
        if set1 != set2:
            set1.update(set2)
            set1[vertex1].append(vertex2)
            self.sets.remove(set2)

    def find(self, vertex):
        for sample_set in self.sets:
            if vertex in sample_set.keys():
                return sample_set


def topological_sort(adjacency_list: Dict[str, List[str]]) -> List[List[str]]:
    """Topological sort of a graph using the Kahn's algorithm.
    Inputs:
    a graph as a disjoint set of adjacency lists
    Returns:
    a set of lists containing the topological sort of our graph
    """

    # Calculate the input degree for each vertex
    in_degree = {}
    for v, adjacents in [(vertex, adjacency_list[vertex]) for vertex in adjacency_list.keys()]:
        in_degree.setdefault(v, 0)
        for adj in adjacents:
            in_degree[adj] = in_degree.get(adj, 0) + 1

    # Enqueue all vertices with input degree 0
    queue = {v for v, count in in_degree.items() if count == 0}
    alphabets = list()

    # One by one dequeue vertices and enqueue adjacents if input degree becomes 0
    for ordered_queue in permutations(queue):
        result = list()
        queue_copy = list(ordered_queue)
        in_degree_copy = in_degree.copy()
        while queue_copy:
            letter = queue_copy.pop(0)
            result.append(letter)

            for adjacent in adjacency_list.get(letter, []):
                in_degree_copy[adjacent] -= 1

                if in_degree_copy[adjacent] == 0:
                    queue_copy.append(adjacent)
        alphabets.append(result)
    return alphabets


def parse_lexicon(lexicon: List[str]) -> DisjointSet:
    """Parse lexicon (collection of words in a fictional language)
    into an adjacency list of characters where an edge a -> b indicates that a goes before b
    """
    alphabet_components = DisjointSet()
    for letter in set("".join(lexicon)):
        alphabet_components.make_set(letter)
    for w1, w2 in zip(lexicon[:-1], lexicon[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                alphabet_components.union(l1, l2)
                break
    return alphabet_components


def _toposort(independent_components: List[List[str]], stack=list()) -> List[List[str]]:
    # 1. Get zero-degree letter from a component and call _toposort for independent components without that letter

    for component in independent_components:
        if component:
            letter = component.pop(0)
            stack.append(letter)
            print(letter, stack)
            yield from _toposort(independent_components, stack)
            component.insert(0, letter)
    yield stack
    if stack:
        stack.pop(-1)


def get_alphabets(lexicon: List[List[str]]) -> List[List[str]]:
    """Obtain all alphabets of a fictional language
    1. Get all topo sorts for every component
    2. Make combinations of the results such that every independent component
        could be injected at any position of another component
    """
    #
    #
    alphabet_components = parse_lexicon(lexicon)
    independent_components = [topological_sort(component) for component in alphabet_components]
    for component_sample in product(*independent_components):
        print(component_sample)
        _toposort(component_sample)

    print(independent_components)

get_alphabets(LEXICON)

# [ [ ['I']],
#   [ ['T', 'A', 'R', 'C', 'M'],
#     ['A', 'T', 'R', 'C', 'M']]]
