import string


class AnagramChecker(object):
    def __init__(self, is_case_sensitive=None):
        if is_case_sensitive is None:
            self.is_case_sensitive = False
        else:
            self.is_case_sensitive = is_case_sensitive

    def check_anagrams(self, sequence1, sequence2):
        if self.is_case_sensitive:
            table = dict.fromkeys(string.ascii_letters, 0)
        else:
            table = dict.fromkeys(string.ascii_lowercase, 0)

        for character in sequence1:
            if not self.is_case_sensitive:
                character = character.lower()
            if character in table:
                table[character] += 1

        for character in sequence2:
            if not self.is_case_sensitive:
                character = character.lower()
            if character in table:
                table[character] -= 1
                if table[character] < 0:
                    return False

        return all(value == 0 for value in table.values())
