import string


class AnagramChecker(object):
    def __init__(self):
            self.table = dict.fromkeys(string.ascii_lowercase, 0)

    def check_anagrams(self, sequence1, sequence2):
        if len(sequence1) != len(sequence2):
            return False
        else:
            return self.compare_words(sequence1.lower(), sequence2.lower())

    def compare_words(self, word1, word2):
        for character in word1:
            if character in self.table:
                self.table[character] += 1
            else:
                raise Exception("Words to compare should only be made up of alphabetical characters.")

        for character in word2:
            if character in self.table:
                self.table[character] -= 1
                if self.table[character] < 0:
                    return False
            else:
                raise Exception("Words to compare should only be made up of alphabetical characters.")
        return all(count == 0 for count in self.table.values())
