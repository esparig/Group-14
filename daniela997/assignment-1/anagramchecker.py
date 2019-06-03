"""This module defines an Anagram checker implementation."""
from collections import Counter

class AnagramChecker(object):
    """Anagram checker with basic functionality.

    Assumes that character case does not matter,
    and inputs should be single words made up of
    alphabetical characters.
    """

    def __init__(self):
        """Creates an anagram checker.
        """

    def check_anagrams(self, sequence1, sequence2):
        """Checks two sequences are anagrams.
        """
        if len(sequence1) != len(sequence2):
            # If length is not the same return false
            return False
        else:
            # Assumes case doesn't matter by default
            return self.compare_words(sequence1.lower(), sequence2.lower())

    def compare_words(self, word1, word2):
        """Compares two words to check if they are
        made up of the same multiset of characters
        using collections.Counter() to count the
        occurrences of each character in the sequences
        """
        return Counter(word1) == Counter(word2)
