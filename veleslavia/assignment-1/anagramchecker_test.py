import unittest

from anagramchecker import AnagramChecker


class TestAnagramChecker(unittest.TestCase):
    def test_identical_strings(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertTrue(checker.check("test", "test"))

    def test_basic(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertTrue(checker.check("listen", "silent"))
        self.assertTrue(checker.check("triangle", "integral"))
        self.assertFalse(checker.check("apple", "pabble"))

    def test_preprocessing(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertTrue(checker.check("test", "test,  "))

    def test_mismatched_len(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertFalse(checker.check("test", "testt"))

    def test_case_sensitive(self):
        checker = AnagramChecker(case_sensitive=True, each_word_in_sentence=False)
        self.assertFalse(checker.check("listen", "Silent"))

    def test_sentences(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=False)
        self.assertTrue(checker.check("Astronomer", "Moon starer"))

    def test_each_word_in_sentence(self):
        checker = AnagramChecker(case_sensitive=False, each_word_in_sentence=True)
        self.assertFalse(checker.check("Astronomer", "Moon starer"))
        self.assertTrue(checker.check("Bored cat night", "Robed act thing"))
