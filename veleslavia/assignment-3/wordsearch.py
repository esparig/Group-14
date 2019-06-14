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
    grid = Grid(letters=[['A', 'A', 'R'], ['T', 'C', 'D']])

    print(set(word for word in grid.traverse(continue_traverse=lexicon.is_prefix) if lexicon.is_word(word)))
