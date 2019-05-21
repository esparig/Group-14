"""This module defines a class which checks if two strings are anagrams."""
from typing import Tuple, Union, List, overload
import re


@overload
def is_anagram(sequence1: List[str], sequence2: List[str]) -> bool: ...
@overload
def is_anagram(sequence1: str, sequence2: str) -> bool: ...


def is_anagram(sequence1, sequence2):
    """Two basic strings are anagrams if their sorted list representations contain exactly the same elements.
     Two sequences of words are anagrams if all the corresponding words are anagrams"""
    if len(sequence1) != len(sequence2):
        return False

    if (type(sequence1) == str) and (type(sequence2) == str):
        return sorted(sequence1) == sorted(sequence2)
    elif (type(sequence1) == list) and (type(sequence2) == list):
        for sq1_word, sq2_word in zip(sequence1, sequence2):
            if not is_anagram(sq1_word, sq2_word):
                return False
        return True


class AnagramChecker(object):

    def __init__(self, case_sensitive: bool, each_word_in_sentence: bool) -> None:
        """

        :param case_sensitive: ignores case differences between words if False
        :param each_word_in_sentence: checks that each word in the first sentence is an anagram
                                    of the corresponding word in the second sentence
        """
        self.case_sensitive = case_sensitive
        self.each_word_in_sentence = each_word_in_sentence

    def preprocess(self, sequence1: str, sequence2: str) -> Union[Tuple[str, str], Tuple[List[str], List[str]]]:
        """Cleans input strings and splits the sentence to words if necessary.
        Doesn't remove numbers but removes special characters
        """
        if not self.case_sensitive:
            sequence1 = sequence1.lower()
            sequence2 = sequence2.lower()

        if self.each_word_in_sentence:
            sequence1 = re.sub('\W+', ' ', sequence1).split()
            sequence2 = re.sub('\W+', ' ', sequence2).split()
        else:
            sequence1 = re.sub('\W+', '', sequence1)
            sequence2 = re.sub('\W+', '', sequence2)
        return sequence1, sequence2

    def check(self, sequence1, sequence2):
        sequence1, sequence2 = self.preprocess(sequence1, sequence2)
        return is_anagram(sequence1, sequence2)
