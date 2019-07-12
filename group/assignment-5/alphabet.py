from collections import defaultdict

dictionary = ["ART", "RAT", "CAT", "CAR", "MI"]
sample_solution = ['A', 'T', 'R', 'C']


class AlphabetSkeleton:
    def __init__(self, dictionary):
        self.graph = defaultdict(list, {letter: [] for letter in set("".join(dictionary))})
        for word1, word2 in zip(dictionary[:-1], dictionary[1:]):
            # find first mismatching character
            # create an edge between mismatching character in word1 and word2
            for letter1, letter2 in zip(word1, word2):
                if letter1 != letter2:
                    self.graph[letter1].append(letter2)
                    break

    def visit_recursively(self, key, is_visited, sorted_alphabet):
        is_visited[key] = True
        for letter in self.graph[key]:
            if not is_visited[letter]:
                self.visit_recursively(letter, is_visited, sorted_alphabet)
        sorted_alphabet.append(key)

    def toposorted(self):
        sorted_alphabet = list()
        is_visited = defaultdict(bool)

        for key in self.graph:
            if not is_visited[key]:
                self.visit_recursively(key, is_visited, sorted_alphabet)
        print(sorted_alphabet[::-1])


alpha = AlphabetSkeleton(dictionary)
alpha.toposorted()
