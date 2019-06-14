from data_structures import Grid, Lexicon


def main():
    """
        for every starting point:
            start traversing the grid
                if path is a prefix:
                    yield path and continue traversing
        filter duplicated words
    """
    lexicon = Lexicon(vocabulary=['CAR', 'CARD', 'CART', 'CAT'])
    grid = Grid(data=[['A', 'A', 'R'], ['T', 'C', 'D']])

    continue_traverse = lambda prefix: lexicon.is_prefix(prefix)
    print(set(word for word in grid.traverse(continue_traverse) if lexicon.is_word(word)))
