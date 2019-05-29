"""This module defines a class which checks if two strings are anagrams."""
from collections import Counter
from functools import singledispatch
import re


@singledispatch
def is_anagram(sequence1, sequence2):
    """Returns True if the two sequences are anagrams.
    """
    raise NotImplemented


@is_anagram.register
def _(sequence1: str, sequence2: str) -> bool:
    """Two basic strings are anagrams if they have the same amount of the same unique characters.
    """
    if len(sequence1) != len(sequence2):
        return False
    return Counter(sequence1) == Counter(sequence2)


@is_anagram.register
def _(sequence1: list, sequence2: list) -> bool:
    """Two sentences are anagram if each corresponding pair of words is an anagram.
    """
    if len(sequence1) != len(sequence2):
        return False
    return all(is_anagram(w1, w2) for w1, w2 in zip(sequence1, sequence2))


def clean_sentence(sentence: str, each_word_in_sentence: bool):
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


def preprocess(sequence: str, case_insensitive: bool, each_word_in_sentence: bool):
    """ Makes anagram case insensitive if need and cleans sentence
    """

    if case_insensitive:
        sequence = sequence.lower()
    return clean_sentence(sequence, each_word_in_sentence)
