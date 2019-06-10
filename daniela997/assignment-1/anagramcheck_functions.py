import re
from collections import Counter


def check_anagrams(sequence1, sequence2, is_case_sensitive=False, word_order_matters=False):
    """Checks two sequences are anagrams.
    Assumes checks are not case sensitive
    and word order does not matter
    in the case of sentence-anagrams
    by default.
    """
    if not is_case_sensitive:
        # If case does not matter convert to lowercase before check.
        sequence1 = sequence1.lower()
        sequence2 = sequence2.lower()

    if word_order_matters:
        # If order matters split into list of strings to be matched.
        sequence2 = sequence2.split()
        sequence1 = sequence1.split()

        if len(sequence1) != len(sequence2):
            return False

        return all(compare_words(cleanup(word1), cleanup(word2))
                   for word1, word2 in zip(sequence1, sequence2))
    else:
        return compare_words(cleanup(sequence1), cleanup(sequence2))


def compare_words(word1, word2):
    """Compares two words to check if they are
    made up of the same multiset of characters
    using collections.Counter() to count
    character occurrences.
    """
    return Counter(word1) == Counter(word2)


def cleanup(sequence):
    """Cleans up character sequences, leaving only
    letters and numbers using regex.
    """
    return re.sub('\S', '', sequence)
