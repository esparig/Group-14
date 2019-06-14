import unittest

from data_structures import Grid, Lexicon


class LexiconTest(unittest.TestCase):
    def test_lexicon(self):
        lexicon = Lexicon(vocabulary=['CAR', 'CARD', 'CART', 'CAT'])

        self.assertTrue(lexicon.is_word('CAR'))
        self.assertTrue(lexicon.is_prefix('CA'))
        self.assertTrue(lexicon.is_prefix('CAT'))
        self.assertTrue(lexicon.is_prefix(''))
        self.assertFalse(lexicon.is_prefix('RAC'))


class GridTest(unittest.TestCase):
    def test_visited_nodes(self):
        grid = Grid(letters=[['A', 'A', 'R'], ['T', 'C', 'D']])
        grid.is_visited[1][2] = True
        self.assertTrue(grid.is_valid_to_visit(0, 1))
        self.assertFalse(grid.is_valid_to_visit(1, 2))
        self.assertFalse(grid.is_valid_to_visit(-1, 0))

    def test_valid_incident(self):
        grid = Grid(letters=[['A', 'A', 'R'], ['T', 'C', 'D']])
        grid.is_visited[0][0] = True
        grid.is_visited[0][2] = True
        valid_incident = set([incident for incident in grid.valid_incident(0, 1)])
        self.assertEqual(valid_incident, set([(1, 0), (1, 1), (1, 2)]))

    def test_traverse_from(self):
        grid = Grid(letters=[['A', 'A', 'R'], ['T', 'C', 'D']])
        condition = lambda x: True
        grid.is_visited[0][0] = True
        grid.is_visited[0][1] = True
        prefix = 'AA'
        words = set([word for word in grid.traverse_from(1, 1, prefix, condition)])
        self.assertEqual(words, set(['AAC', 'AACT', 'AACD', 'AACDR', 'AACR', 'AACRD']))


class WordSearchTest(unittest.TestCase):
    def test_traverse_with_condition(self):
        lexicon = Lexicon(vocabulary=['CAR', 'CARD', 'CART', 'CAT'])
        grid = Grid(letters=[['A', 'A', 'R'], ['T', 'C', 'D']])

        in_lexicon = set(word for word in grid.traverse(continue_traverse=lexicon.is_prefix) if lexicon.is_word(word))
        self.assertEqual(in_lexicon, set(['CAT', 'CARD', 'CAR']))
