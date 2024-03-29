"""Example usage of linkedlist.py and klast.py."""

import sys

import klast
import linkedlist


def test():
  lexicon = Lexicon()
  lexicon.add_words("CAR", "CAT", "CARD", "CART")
  grid1 = [["A", "A", "R"], ["T", "C", "D"]]
  words = list(search_grid(grid1, lexicon))
  words.reverse()
  print(words)


test()

def main(args):
  list_ = linkedlist.LinkedList(args)
  for node in list_:
    print(node.value)

  for k in range(len(args)):
    node = klast.get_k_to_last(list_, k)
    if node:
      print('%d: %s' % (k, node.value))
    else:
      print('%d: -' % k)

  for k in range(len(args)):
    node = klast.get_k_to_last_one_pass(list_, k)
    if node:
      print('%d: %s' % (k, node.value))
    else:
      print('%d: -' % k)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
