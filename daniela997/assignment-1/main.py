import sys

from anagramchecker_extended import AnagramChecker


def main(args):
    anagram_checker = AnagramChecker(is_case_sensitive=False, word_order_matters=False)
    input1 = str(input("Enter first sequence: "))
    input2 = str(input("Enter second sequence: "))
    if anagram_checker.check_anagrams(input1, input2):
        print("The sequences are anagrams!")
    else:
        print("The sequences are not anagrams!")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
