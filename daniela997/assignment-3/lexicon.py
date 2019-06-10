"""Lexicon implementation uses the concept of a trie.
"""


class LetterNode:
    def __init__(self):
        """Trie node, can have 0 or more children.
        If the represented letter is also the last letter
        in a word in the lexicon, the node is a terminating one.
        """
        self.children = {}
        self.is_terminating = False

    def __repr__(self):
        """Text representation for debugging purposes
        - it does not print a nice-looking trie... :-)
        """
        for child in self.children:
            print(self.children.get(child))
        return ' '.join(chr(child + ord('A')) for child in self.children)


class Lexicon:
    """A Lexicon is a trie built of LetterNodes.
    """
    def __init__(self):
        """Root is a parentless node.
        """
        self.root = LetterNode()

    def __repr__(self):
        return repr(self.root)

    def get_child_index(self, child_character):
        """Calculates an index under which a child node
        will be stored in the self.children dictionary
        for the parent.

        :param child_character: child character to calculate
        index for
        :return: int representing the child's index
        """
        return ord(child_character) - ord('A')

    def add_words(self, *args):
        """
        Adds to the Lexicon, representing each character as a
        LetterNode.
        :param args: words to be added
        """
        for word in args:
            current_node = self.root
            for char in word:
                # Traverse words character by character
                index = self.get_child_index(char)
                if index not in current_node.children:
                    # If the character's index is not in the current node's children, add it
                    current_node.children[index] = LetterNode()
                # Travel down the trie branch
                current_node = current_node.children.get(index)
            # When last character is reached, note that its node is a terminating one
            current_node.is_terminating = True

    def is_word(self, word):
        """Checks if a word is in the Lexicon.
        :param word: word to search for
        :return: True/False if word is in the Lexicon or not
        """
        # Word is a prefix whose last character is a terminating node
        last_node = self._is_prefix_check(word)
        return True if last_node and last_node.is_terminating else False

    def is_prefix(self, prefix):
        """Checks if a string is a prefix to at least 1 word in the lexicon.
        :param prefix: prefix to search for
        :return: True/False if prefix is in the Lexicon or not
        """
        return True if self._is_prefix_check(prefix) else False

    def _is_prefix_check(self, prefix):
        """Checks if prefix is in lexicon. Helper used by is_prefix and is_word.
        :param prefix: prefix to search for
        :return: Last node of found prefix - None if prefix is not found
        """
        if len(prefix) == 0:
            return None
        current_node = self.root
        # For each character, walk down trie and check if prefix is represented as a trie branch
        for char in prefix:
            index = self.get_child_index(char)
            if not current_node:
                return None
            current_node = current_node.children.get(index)
        return current_node


