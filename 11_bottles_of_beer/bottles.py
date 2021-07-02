#!/usr/bin/env python3
"""
Purpose: Count down the numbers of bottles on the wall.
"""

import argparse

VERSE_TEMPLATE = '''{number} bottle{s} of beer on the wall,
{number} bottle{s} of beer,
Take one down, pass it around,
{next_number} bottle{s_next} of beer on the wall!'''


def get_args():
    """Get args from the command line."""
    parser = argparse.ArgumentParser(
        description='Count down the number of bottles on the wall',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        default=10,
                        type=int)

    args = parser.parse_args()
    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')
    return args


def main():
    """Print the verses of the song."""
    args = get_args()
    for i in range(args.number, 0, -1):
        next_number = i - 1
        plural = '' if i == 1 else 's'
        plural_next = '' if next_number == 1 else 's'
        new_line = '\n' if next_number else ''
        if next_number == 0:
            next_number = 'No more'
        print(
            VERSE_TEMPLATE.format(
                number=i, next_number=next_number, s=plural, s_next=plural_next)
            + new_line)


if __name__ == '__main__':
    main()
