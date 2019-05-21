import collections

def anagrams_case_sensitive(str1: str, str2: str) -> bool:
    a = collections.Counter(str1)
    for c in str2:
        a[c] -= 1
        if a[c] < 0:
            return False
    return sum(a.values()) == 0

def anagrams(str1: str, str2: str, case_insensitive: bool=False) -> bool:
    if case_insensitive:
        return anagrams_case_sensitive(str1.lower(), str2.lower())
    else:
        return anagrams_case_sensitive(str1, str2)
    