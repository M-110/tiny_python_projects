#!/usr/bin/env python3
"""
Purpose: Look up lines within a text file which begin with the letter passed
into the command.
"""

import argparse


def get_args():
    """Get arguments from the command line."""
    parser = argparse.ArgumentParser(
        description='Look lines beginning with a certain letter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('letters',
                        metavar='str',
                        help='Letters to look up',
                        nargs='+',
                        typr=str)
    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='File to look up in',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')
    return parser.parse_args()


def main():
    """Print the lines which begin with the letter given by the command line
     argument"""
    args = get_args()
    file = args.file
    letters = args.letters
    file = file.read().split('\n')

    first_letters = ''.join([line[0].lower() for line in file if line])
    positions = [first_letters.find(letter.lower()) for letter in letters]

    for letter, position in zip(letters, positions):
        if position == -1:
            print(f'I do not know "{letter}".')
        else:
            print(file[position])


if __name__ == '__main__':
    main()
