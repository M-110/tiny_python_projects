#!/usr/bin/env python
"""
Purpose: To sing the 12 days of Christmas.
"""

import argparse
import sys

GIFTS = [
    'A partridge in a pear tree', 'Two turtle doves', 'Three French hens',
    'Four calling birds', 'Five gold rings', 'Six geese a laying',
    'Seven swans a swimming', 'Eight maids a milking', 'Nine ladies dancing',
    'Ten lords a leaping', 'Eleven pipers piping', 'Twelve drummers drumming'
]

ORDINALS = [
    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
    'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
]


def get_args():
    """Get args from command line."""
    parser = argparse.ArgumentParser(
        description='Singer of the 12 days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n',
                        '--num',
                        metavar='days',
                        type=int,
                        help='Number of days',
                        default=12,
                        dest='days')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Output file location',
                        default=sys.stdout,
                        dest='file')
    args = parser.parse_args()
    if args.days < 0 or args.days > 12:
        parser.error(f'--num "{args.days}" must be between 1 and 12')
    return args


def verse(day: int) -> list:
    """Print a verse of the song."""
    verse_lines = [
        f'On the {ORDINALS[day]} day of Christmas,', 'My true love gave to me,'
    ]
    for i in range(day, -1, -1):
        if i == 0:
            if day == 0:
                verse_lines.append(f'{GIFTS[i]}.')
            else:
                verse_lines.append(f'And {GIFTS[i].lower()}.')
        else:
            verse_lines.append(f'{GIFTS[i]},')
    return verse_lines


def main():
    """Print or save the file for the twelve days of Christmas."""
    args = get_args()
    for i in range(args.days):
        args.file.write('\n'.join(verse(i)))
        if i != args.days - 1:
            args.file.write('\n\n')


if __name__ == '__main__':
    main()
