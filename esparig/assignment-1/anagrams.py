"""First assignment: Anagrams"""
from collections import Counter

def anagrams_case_sensitive(str1: str, str2: str) -> bool:
    """Function to analyze if two strings are anagrams"""
    dict1 = Counter(str1)
    for char in str2:
        dict1[char] -= 1
        if dict1[char] < 0:
            return False
    return sum(dict1.values()) == 0


def anagrams(str1: str, str2: str, case_insensitive: bool = False,
             is_sentence: bool = False, corresponding_words: bool = False) -> bool:
    """Fuction to analyze if two strings are anagrams considering case sensitivity and sentences"""
    if is_sentence:
        if corresponding_words:
            pass #TO DO
        else:
            str1 = ''.join([i for i in str1 if i.isalnum()])
            str2 = ''.join([i for i in str2 if i.isalnum()])
    if case_insensitive:
        return anagrams_case_sensitive(str1.lower(), str2.lower())
    return anagrams_case_sensitive(str1, str2)
