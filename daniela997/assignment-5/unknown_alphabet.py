import sys
from directed_acyclic_graph import DirectedAcyclicGraph


def parse_lexicon(lexicon, graph):
    """
    Given a DAG object and a lexicon, populate
    the graph such that for each unique character found in the lexicon
    there is a vertex in the graph
    :param lexicon: list of words
    :param graph: directed acyclic graph to add vertices to
    """
    # Walk the lexicon with a 2x sliding window
    for i in range(1, len(lexicon)):
        # For each couple of consecutive words find the
        # first position where characters are different
        # and create an edge in the graph between the vertices
        # for those characters
        word1, word2 = lexicon[i], lexicon[i-1]
        for a, b in zip(word1, word2):
            if a != b:
                graph.add_edge(a, b)
                break


def main(args):
    lexicon = ["ART", "RAT", "CAT", "CAR"]
    graph = DirectedAcyclicGraph()
    parse_lexicon(lexicon, graph)
    print("Alphabet order: ")
    print(graph.topological_sort())


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
