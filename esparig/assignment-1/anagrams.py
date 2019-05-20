import collections
from jedi.settings import case_insensitive_completion
from numba import lowering

def anagrams0(str1, str2):

    return (sum(collections.Counter(str1).values()) - sum(collections.Counter(str2).values())) == 0

def anagrams1(str1, str2):
    a = collections.Counter(str1)
    for c in str2:
        a[c] -= 1
        if a[c] < 0:
            return False
    return sum(a.values()) == 0

def anagrams2(str1, str2, case_insensitive=False):
    if case_insensitive == True:
        str1 = str1.lower()
        str2 = str2.lower()

    a = collections.Counter(str1)
    for c in str2:
        a[c] -= 1
        if a[c] < 0:
            return False
    return sum(a.values()) == 0