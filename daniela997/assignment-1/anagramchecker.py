import string


class AnagramChecker(object):
    def __init__(self, is_case_sensitive=None, word_order_matters=None):
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
        if not self.is_case_sensitive:
            sequence1 = sequence1.lower()
            sequence2 = sequence2.lower()

        if self.word_order_matters:
            sequence2 = sequence2.split()
            sequence1 = sequence1.split()

            if len(sequence1) != len(sequence2):
                return False

            for word1, word2 in zip(sequence1, sequence2):
                anagram_pair = self.compare_words(word1, word2)

                self.table = self.table.fromkeys(self.table, 0)

                if not anagram_pair:
                    return False
            return True
        else:
            return self.compare_words(sequence1, sequence2)

    def compare_words(self, word1, word2):
        for character in word1:
            if character in self.table:
                self.table[character] += 1

        for character in word2:
            if character in self.table:
                self.table[character] -= 1
                if self.table[character] < 0:
                    return False
        return all(count == 0 for count in self.table.values())
