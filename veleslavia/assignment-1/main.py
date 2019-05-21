import argparse

from anagramchecker import AnagramChecker


def main(args):
    checker = AnagramChecker(args.case_sensitive, args.each_word_in_sentence)
    print(f"First sequence to process: {args.sequence1} \n"
          f"Second sequence to process: {args.sequence2} \n"
          f"Checker is case sensitive: {args.case_sensitive} \n"
          f"Checking word-by-word anagrams: {args.each_word_in_sentence} \n"
          f"Two strings are anagrams: {checker.check(args.sequence1, args.sequence2)}.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process parameters of the anagram checker.')
    parser.add_argument('--case_sensitive', action='store_true', help='make the checker case sensitive')
    parser.add_argument('--each_word_in_sentence', action='store_true',
                        help='ensure that every corresponding pair of words in two sentences are anagrams of each other')
    parser.add_argument('sequence1', help='make sure to put quotes if a sentence is to be handled')
    parser.add_argument('sequence2', help='make sure to put quotes if a sentence is to be handled')
    args = parser.parse_args()
    main(args)
