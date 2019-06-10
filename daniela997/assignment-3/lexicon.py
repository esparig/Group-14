class LetterNode:
    def __init__(self):
        self.children = {}
        self.is_terminating = False

    def __repr__(self):
        for child in self.children:
            print(self.children.get(child))
        return ' | '.join(chr(child + ord('A')) for child in self.children)


class Lexicon:
    def __init__(self):
        self.root = LetterNode()

    def __repr__(self):
        return repr(self.root)

    def get_child_index(self, child_character):
        return ord(child_character) - ord('A')

    def add_words(self, *args):
        for word in args:
            current_node = self.root
            for char in word:
                index = self.get_child_index(char)
                if index not in current_node.children:
                    current_node.children[index] = LetterNode()
                current_node = current_node.children.get(index)
            current_node.is_terminating = True

    def is_word(self, word):
        last_node = self._is_prefix_check(word)
        return True if last_node and last_node.is_terminating else False

    def is_prefix(self, word):
        return True if self._is_prefix_check(word) else False

    def _is_prefix_check(self, word):
        if len(word) == 0:
            return False
        current_node = self.root
        for char in word:
            index = self.get_child_index(char)
            if not current_node:
                return False
            current_node = current_node.children.get(index)
        return current_node


