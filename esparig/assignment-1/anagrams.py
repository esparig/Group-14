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
    """Function to analyze if two strings are anagrams considering case sensitivity and sentences"""
    if is_sentence:
        if corresponding_words:
            list_str1, list_str2 = str1.split(), str2.split()
            if len(list_str1) != len(list_str2):
                return False
            if case_insensitive:
                list_str1 = [s.lower() for s in list_str1]
                list_str2 = [s.lower() for s in list_str2]
            for i in range(len(list_str1)):
                if not anagrams_case_sensitive(list_str1[i].lower(), list_str2[i].lower()):
                    return False
            return True
        else:
            str1 = ''.join([i for i in str1 if i.isalnum()])
            str2 = ''.join([i for i in str2 if i.isalnum()])
    if case_insensitive:
        return anagrams_case_sensitive(str1.lower(), str2.lower())
    return anagrams_case_sensitive(str1, str2)
