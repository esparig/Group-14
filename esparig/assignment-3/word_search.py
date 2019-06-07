"""
Assignment 3: Word Search.
"""
from typing import List

class Lexicon:
    def __init__(self, chr: str, ends: bool, next: List['Lexicon']) -> None:
        self.chr = chr
        self.ends = ends
        self.next = next
    
    def is_word(self, word: List[str]) -> bool:
        """Takes a string as a list of characters and returns whether the string is a word in the lexicon
        """
        if len(word) == 0:
            return self.ends
        
        for elem in self.next:
            if word[0] == elem.chr:
                return elem.is_word(word[1:])
    
    def is_preffix(self, preffix):
        if len(preffix) == 0:
            return True
        
        for elem in self.next:
            if preffix[0] == elem.chr:
                return elem.is_preffix(preffix[1:])
        
        