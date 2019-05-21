"""This module defines an Anagram checker implementation."""
import string


class AnagramChecker(object):
    """Anagram checker with extended functionality.

    Anagram sequences can be single words or whole sentences; white space
    and punctuation is ignored.
    """

    def __init__(self, is_case_sensitive=None, word_order_matters=None):
        """Creates an anagram checker. It uses a hash table to perform checks.

        Args:
            is_case_sensitive: whether check should be case sensitive or not.
            word_order_matters: whether order of letters is tied to words or not.
        """
        if is_case_sensitive is None:
            self.is_case_sensitive = False
            self.table = dict.fromkeys(string.ascii_lowercase, 0)
        else:
            self.is_case_sensitive = is_case_sensitive
            if is_case_sensitive:
                self.table = dict.fromkeys(string.ascii_letters, 0)
            else:
                self.table = dict.fromkeys(string.ascii_lowercase, 0)

        if word_order_matters is None:
            self.word_order_matters = False
        else:
            self.word_order_matters = word_order_matters

    def check_anagrams(self, sequence1, sequence2):
        """Checks two sequences are anagrams.
        """
        if not self.is_case_sensitive:
            # If case does not matter convert to lowercase before check.
            sequence1 = sequence1.lower()
            sequence2 = sequence2.lower()

        if self.word_order_matters:
            # If order matters split into list of strings to be matched.
            sequence2 = sequence2.split()
            sequence1 = sequence1.split()

            if len(sequence1) != len(sequence2):
                return False

            for word1, word2 in zip(sequence1, sequence2):
                # Perform check for each pair of words.
                anagram_pair = self.compare_words(word1, word2)

                self.table = self.table.fromkeys(self.table, 0)

                if not anagram_pair:
                    return False
            return True
        else:
            return self.compare_words(sequence1, sequence2)

    def compare_words(self, word1, word2):
        """Compares two words to check if they are
        made up of the same multiset of characters
        using a dictionary of counters for every
        letter in the alphabet.
        """
        for character in word1:
            if character in self.table:
                self.table[character] += 1

        for character in word2:
            if character in self.table:
                self.table[character] -= 1
                if self.table[character] < 0:
                    return False
        return all(count == 0 for count in self.table.values())
