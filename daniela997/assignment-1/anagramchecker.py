"""This module defines an Anagram checker implementation."""
import string


class AnagramChecker(object):
    """Anagram checker with basic functionality.

    Assumes that character case does not matter,
    and inputs should be single words made up of
    alphabetical characters.
    """
    def __init__(self):
        """Creates an anagram checker.
        """
        self.table = dict.fromkeys(string.ascii_lowercase, 0)

    def check_anagrams(self, sequence1, sequence2):
        """Checks two sequences are anagrams.
        """
        if len(sequence1) != len(sequence2):
            # If length is not the same return false
            return False
        else:
            return self.compare_words(sequence1.lower(), sequence2.lower())

    def compare_words(self, word1, word2):
        """Compares two words to check if they are
        made up of the same multiset of characters
        using a dictionary of counters for every
        letter in the alphabet.
        """
        for character in word1:
            if character in self.table:
                self.table[character] += 1
            else:
                raise Exception("Words to compare should only be made up of alphabetical characters.")

        for character in word2:
            if character in self.table:
                self.table[character] -= 1
                if self.table[character] < 0:
                    # If counter is negative we can be sure words are not anagrams.
                    return False
            else:
                raise Exception("Words to compare should only be made up of alphabetical characters.")
        return all(count == 0 for count in self.table.values())
