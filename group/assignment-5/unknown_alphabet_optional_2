"""Given a lexicon of all words in lexicographic order of a fictional Language
find the alphabet of that Language
"""
from typing import List, DefaultDict, Set
from collections import defaultdict

def topological_sort(adjacency_list: DefaultDict[str, List[str]]) -> List[str]:
    """Topological sort of a graph using the Kahn's algorithm.
    Inputs:
    a graph as an adjacency list
    Returns:
    a list containing the topological sort of our graph
    """
    
    # Calculate the input degree for each vertex
    in_degree = {}
    for v, adjacents in [(vertex, adjacency_list[vertex]) for vertex in adjacency_list.keys()]:
        in_degree.setdefault(v, 0)
        for adj in adjacents:
            in_degree[adj] = in_degree.get(adj, 0) + 1
    
    # Enqueue all vertices with input degree 0        
    queue = {v for v, count in in_degree.items() if count == 0}
    result = []
    
    # One by one dequeue vertices and enqueue adjacents if input degree becomes 0 
    while queue:
        v = queue.pop()
        result.append(v)
        
        for adjacent in adjacency_list.get(v, []):
            in_degree[adjacent] -= 1
            
            if in_degree[adjacent] == 0:
                queue.add(adjacent)
    
    # Check for cycles in the graph
    if len(result) != len(in_degree):
        # Cycles mean one letter comes both before and after another
        print("Lexicon has inconsistent rules: ")
        inconsistent = list(set(in_degree.keys())-set(result))
        for i in inconsistent:
            for adj in adjacency_list[i]:
              if adj in inconsistent and i in adjacency_list[adj]:
                print("{} comes before {}".format(i, adj))
        # raise SyntaxError(f"The graph provided is not a DAG")
        return
    else:
        return result

def parse_lexicon(lexicon: List[List[str]]) -> DefaultDict[str, List[str]]:
    """Parse lexicon (collection of words in a fictional language)
    into an adjacency list of characters where an edge a -> b indicates that a goes before b
    """
    adj_list = defaultdict(list, {letter: [] for letter in set("".join(lexicon))})
    #set([chr for word in lexicon for chr in word])

    for w1, w2 in zip(lexicon[:-1], lexicon[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                adj_list[l1].append(l2)
                break

    return adj_list

def get_alphabet(lexicon: List[List[str]]) -> List[str]:
    """Obtain the alphabet in lexicographic order of a fictional language
    """
    return topological_sort(parse_lexicon(lexicon))
