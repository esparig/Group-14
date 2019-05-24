"""First assignment: Anagrams"""
from collections import Counter
from typing import List

def compare(str1: str, str2: str) -> bool:
    """Function to analyze if two strings are anagrams"""
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)

def compare_list(str1: List[str], str2: List[str]) -> bool:
    """Function to analyze if two lists contains corresponding anagrams"""
    if len(str1) != len(str2):
        return False
    for word1, word2 in zip(str1, str2):
        if not compare(word1, word2):
            return False
    return True

def normalize(string: str, case_sensitive: bool, is_sentence: bool,
              corresponding_words: bool) -> List[str]:
    """Function to normalize string according to options"""
    if not case_sensitive:
        string = string.lower()
    if is_sentence:
        if corresponding_words:
            string = string.split()
            return string
        string = ''.join([i for i in string if i.isalnum()])
    return [string]

def anagrams(str1: str, str2: str, case_sensitive: bool = True,
             is_sentence: bool = False, corresponding_words: bool = False) -> bool:
    """Function to analyze if two strings are anagrams considering case sensitivity and sentences"""
    return compare_list(normalize(str1, case_sensitive, is_sentence, corresponding_words),
                        normalize(str2, case_sensitive, is_sentence, corresponding_words))
