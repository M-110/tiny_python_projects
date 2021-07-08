#!/usr/bin/env python
"""
Purpose: Create a ransom note!
"""

import argparse
import random


def get_args():
    """Get args from command line."""
    parser = argparse.ArgumentParser(
        description='Convert text to ransom style',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', type=str, help='Text or file to convert')
    parser.add_argument('-s', '--seed', type=int, help='Random seed number',
                        default=None)
    return parser.parse_args()


def main():
    """Print a ransom version of the text."""
    args = get_args()
    text = args.text
    if '.txt' in text:
        with open(text) as file:
            text = file.read()
    random.seed(args.seed)
    text = ''.join([char.upper() if random.choice([False, True]) else char.lower()
                    for char in text])
    print(text)


if __name__ == '__main__':
    main()
