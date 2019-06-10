import sys

from lexicon import Lexicon
from search_grid import search_grid


def main(args):
    lexicon = Lexicon()
    lexicon.add_words("CAR", "CAT", "CARD", "CART")
    grid = [["A", "A", "R"], ["T", "C", "D"]]
    words = list(search_grid(grid, lexicon))
    words.reverse()
    print(words)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
