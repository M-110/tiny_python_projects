#!/usr/bin/env python
"""
Purpose: Convert text to sound more like a Kentucky accent.
"""

import argparse
import os
import re

SOUTHERN_DICT = {}
with open('southern_dict.txt', encoding='utf8') as file:
    for line in file:
        key, value = line.split('|')
        SOUTHERN_DICT[key.strip()] = value.strip()


def get_args():
    """Get args from command line."""
    parser = argparse.ArgumentParser(
        description='Convert text to sound southern',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text', type=str, help='Text to convert')
    args = parser.parse_args()
    if os.path.isfile(args.text):
        with open(args.text, encoding='utf8') as file:
            args.text = file.read()
    return args


def drop_the_g(text: str) -> str:
    """Remove the g from the ending "-ing" on any two syllable word"""
    pattern = r'(\w+[aeiouy]\w*in)(g)\b'
    return re.sub(pattern, r"\1'", text, flags=re.IGNORECASE)


def you_to_yall(text: str) -> str:
    """Convert all you's to y'all."""
    for key, value in SOUTHERN_DICT.items():
        pattern = r'\b' + key + r'\b'
        text = re.sub(pattern, value, text, flags=re.IGNORECASE)
    return text


def main():
    """Get args and print them in a southern accent."""
    text = get_args().text
    text = drop_the_g(text)
    text = you_to_yall(text)
    print(text)


if __name__ == '__main__':
    main()
