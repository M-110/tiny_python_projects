#!/usr/bin/env python
"""
Purpose: An interactive game of mad libs.
"""
import argparse
import re
import sys
from typing import List


def get_args():
    """Get arguments from the command line."""
    parser = argparse.ArgumentParser(
        description='A game of mad libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('file',
                        metavar='FILE',
                        help='File containing the mad libs text',
                        type=argparse.FileType('rt'))
    parser.add_argument('-i',
                        '--inputs',
                        type=str,
                        nargs='*',
                        help='Optional input arguments')
    return parser.parse_args()


def find_placeholders(filename: str, text: str) -> List[str]:
    """Parse the input file and return a list of the placeholders.

    Quits if no placeholders are found.
    """
    if placeholders := re.findall(r'<.*?>', text):
        return placeholders
    print(f'"{filename}" has no placeholders.')
    sys.exit(2)


def get_user_inputs(placeholders: List[str]) -> List[str]:
    """Get an input from user for each placeholder"""
    inputs = []
    for placeholder in placeholders:
        inputs.append(input(f'Give me {a_or_an(placeholder)}'))
    return inputs


def a_or_an(text: str) -> str:
    """Returns the text with the proper a or an article before it."""
    article = 'an' if text[1] in 'aeiou' else 'a'
    return f'{article} {text[1:-1]}'


def substitute_inputs(text: str, placeholders: List[str],
                      inputs: List[str]) -> str:
    """Substitute the inputs for the placeholders in the text"""
    for placeholder, replacement in zip(placeholders, inputs):
        text = re.sub(placeholder, replacement, text, 1)
    return text


def main():
    """Get arguments and print out the mad lib."""
    args = get_args()
    text = args.file.read()
    placeholders = find_placeholders(args.file.name, text)
    if args.inputs:
        inputs = args.inputs
    else:
        inputs = get_user_inputs(placeholders)
    output = substitute_inputs(text, placeholders, inputs)
    print(output)


if __name__ == '__main__':
    main()
