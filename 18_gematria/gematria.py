#!/usr/bin/env python
"""
Purse: Translate words into numbers.
"""

import argparse
import re


def get_args():
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description='Translates words to numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', type=str, help='Text or file to translate')
    return parser.parse_args()


def translate(text: str) -> str:
    """Replace all words with their numeric translation."""
    return re.sub(r'\S+', lambda x: sum_word(x[0]), text)


def sum_word(word: str) -> str:
    """Sum the ordinal values of a word."""
    return str(sum([ord(char) for char in word if char.isalnum()]))


def main():
    """Get arguments and print the translated words as numbers."""
    args = get_args()
    if '.txt' in args.text:
        with open(args.text) as file:
            args.text = file.read()
    translation = translate(args.text)
    print(translation)


if __name__ == '__main__':
    main()
