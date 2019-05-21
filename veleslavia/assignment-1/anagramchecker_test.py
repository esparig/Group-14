import unittest

from anagramchecker import AnagramChecker


class TestAnagramChecker(unittest.TestCase):
    def test_identical_strings(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertEqual(checker.check("test", "test"), True)

    def test_basic(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertEqual(checker.check("listen", "silent"), True)
        self.assertEqual(checker.check("triangle", "integral"), True)
        self.assertEqual(checker.check("apple", "pabble"), False)

    def test_preprocessing(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertEqual(checker.check("test", "test,  "), True)

    def test_mismatched_len(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertEqual(checker.check("test", "testt"), False)

    def test_case_sensitive(self):
        checker = AnagramChecker(case_sensitive=True, each_word_in_sentence=False)
        self.assertEqual(checker.check("listen", "Silent"), False)

    def test_sentences(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertEqual(checker.check("Astronomer", "Moon starer"), True)

    def test_each_word_in_sentence(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=True)
        self.assertEqual(checker.check("Astronomer", "Moon starer"), False)
        self.assertEqual(checker.check("Bored cat night", "Robed act thing"), True)
