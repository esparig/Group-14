"""This module defines a class which checks if two strings are anagrams."""
from typing import Union, List, overload
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


def clean_sentence(sentence: str, each_word_in_sentence: bool) -> Union[str, List[str]]:
    """ Cleans input strings and splits the sentence to words if necessary.
        Doesn't remove numbers but removes special characters
    :param sentence: sentence to be processed
    :param each_word_in_sentence: checks that each word in the first sentence is an anagram
                                of the corresponding word in the second sentence
    :return: sentence without spaces and punctuation or list of words
    """
    if each_word_in_sentence:
        sentence = re.sub('\W+', ' ', sentence).split()
    else:
        sentence = re.sub('\W+', '', sentence)
    return sentence


def preprocess(sequence: str, case_insensitive: bool, each_word_in_sentence: bool) -> Union[str, List[str]]:
    """ Makes anagram case insensitive if need and cleans sentence
    """

    if case_insensitive:
        sequence = sequence.lower()
    return clean_sentence(sequence, each_word_in_sentence)
