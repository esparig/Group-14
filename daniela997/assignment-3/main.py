"""Example usage of lexicon.py and search_grid.py"""

import sys

from lexicon import Lexicon
from search_grid import search_grid


def main(args):
    lexicon = Lexicon()
    lexicon.add_words("CAR", "CAT", "CARD", "CART")
    lexicon2 = Lexicon()
    lexicon2.add_words("CAT")
    print(lexicon2)
    grid = [["A", "A", "R"], ["T", "C", "D"]]
    words = list(search_grid(grid, lexicon))
    # Reversing so it prints results out in the order shown in the pdf
    words.reverse()
    print(words)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
