import unittest

from anagramchecker import AnagramChecker


class AnagramCheckerTest(unittest.TestCase):
    def test_baseline_functionality(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("stressed", "desserts"))
        self.assertFalse(anagram_checker.check_anagrams("stressed", "dessert"))

    def test_same_words(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("listen", "silent"))
        self.assertFalse(anagram_checker.check_anagrams("listens", "silent"))

    def test_same_length(self):
        anagram_checker = AnagramChecker()
        self.assertTrue(anagram_checker.check_anagrams("cat", "act"))
        self.assertFalse(anagram_checker.check_anagrams("apple", "pabble"))


if __name__ == '__main__':
    unittest.main()
