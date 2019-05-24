import unittest
from functools import partial

from anagramchecker import is_anagram, preprocess


class TestAnagramChecker(unittest.TestCase):
    def test_identical_strings(self):
        self.assertTrue(is_anagram("test", "test"))

    def test_basic(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("apple", "pabble"))

    def test_clean_sentence(self):
        parametrized_preprocess = partial(preprocess,
                                          case_insensitive=False,
                                          each_word_in_sentence=False)
        self.assertEqual(parametrized_preprocess("test,   "), parametrized_preprocess("test"))

    def test_case_insensitive(self):
        parametrized_preprocess = partial(preprocess,
                                          case_insensitive=True,
                                          each_word_in_sentence=False)
        self.assertEqual(parametrized_preprocess("Silent"), 'silent')

    def test_sentences(self):
        parametrized_preprocess = partial(preprocess,
                                          case_insensitive=True,
                                          each_word_in_sentence=False)
        self.assertTrue(is_anagram(parametrized_preprocess("Astronomer"),
                                   parametrized_preprocess("Moon starer")))

    def test_each_word_in_sentence(self):
        parametrized_preprocess = partial(preprocess,
                                          case_insensitive=True,
                                          each_word_in_sentence=True)
        self.assertFalse(is_anagram(parametrized_preprocess("Astronomer"),
                                    parametrized_preprocess("Moon starer")))
        self.assertTrue(is_anagram(parametrized_preprocess("Bored cat night"),
                                   parametrized_preprocess("Robed act thing")))
