"""Given a lexicon of all words in lexicographic order of a fictional Language
find all alphabets of that Language
"""
from typing import List, Dict, DefaultDict, Tuple, Set
from collections import defaultdict


def parse_lexicon(lexicon: List[List[str]]) -> DefaultDict[str, List[str]]:
    """Parse lexicon (collection of words in a fictional language)
    into an adjacency list of characters where an edge a -> b indicates that a goes before b
    """
    adj_list = defaultdict(list, {letter: [] for letter in set("".join(lexicon))})

    for w1, w2 in zip(lexicon[:-1], lexicon[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                adj_list[l1].append(l2)
                break

    return adj_list


def topological_sort(adjacency_list: Dict[str, List[str]], in_degree: Dict, result: List[str]):
    """Topological sort of a graph using the Kahn's algorithm.
    Inputs:
    a graph as an adjacency list
    in_degree as a dictionary with input degree of every vertex
    result as a prominent alphabet
    Returns:
    a generator which returns tuples containing a topological sort of the graph
    """
    if not in_degree:
        # Calculate the input degree for each vertex
        in_degree = {}
        for v, adjacents in [(vertex, adjacency_list[vertex]) for vertex in adjacency_list.keys()]:
            in_degree.setdefault(v, 0)
            for adj in adjacents:
                in_degree[adj] = in_degree.get(adj, 0) + 1

    queue = {v for v, count in in_degree.items() if count == 0}

    for v in queue:
        in_degree[v] -= 1
        result.append(v)
        for adj in adjacency_list[v]:
            in_degree[adj] -= 1
        yield from topological_sort(adjacency_list, in_degree, result)
        for adj in adjacency_list[v]:
            in_degree[adj] += 1
        if all(in_degree[key] == -1 for key in in_degree.keys()):
            yield tuple(result.copy())
        result.remove(v)
        in_degree[v] += 1


def get_alphabets(lexicon: List[str]) -> Set[List[str]]:
    alphabets = set()
    alphabet_components = parse_lexicon(lexicon)
    for sample_alphabet in topological_sort(alphabet_components, in_degree=None, result=[]):
        alphabets.add(sample_alphabet)

    return alphabets
