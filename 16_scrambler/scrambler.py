#!/usr/bin/env python
"""
Purpose: Randomly scramble the letters of a text.
"""

import argparse
import random
import re
from typing import List


def get_args():
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(
        description='Scramble!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', type=str, help='Text to scramble')
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        help='Random seed',
                        default=None)
    return parser.parse_args()


def scramble_word(word: str) -> str:
    """Return a scrambled version of the word."""
    return ''.join(random.sample(word, k=len(word)))


def get_words(text: str) -> List[str]:
    """Get a list of words in the text."""
    return re.split(r'\b', text)


def main():
    """Get arguments and print the scrambled text."""
    args = get_args()
    random.seed(args.seed)
    words = get_words(args.text)
    text = ''.join([scramble_word(word) for word in words])
    print(text)


if __name__ == '__main__':
    main()
