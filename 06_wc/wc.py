#!/usr/bin/env python3
"""
Purpose: Count the lines, words and bytes within an input file.
"""

import argparse
import sys


def get_args():
    """Get args from the command line."""
    parser = argparse.ArgumentParser(
        description='Word count',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('command',
                        nargs='?',
                        metavar='str',
                        help='Linux-like command to apply to the file',
                        choices=['count', 'cat', 'head', 'tail', 'tac'])
    parser.add_argument('files',
                        metavar='FILE',
                        help='File(s) to be counted.',
                        nargs='*',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'))
    parser.add_argument('-b',
                        '--bytes',
                        help='Display bytes count',
                        action='store_true')
    parser.add_argument('-l',
                        '--lines',
                        help='Display line count',
                        action='store_true')
    parser.add_argument('-w',
                        '--words',
                        help='Display word count',
                        action='store_true')
    parser.add_argument('-c',
                        '--characters',
                        help='Number of characters to display',
                        metavar='int',
                        type=int,
                        default=50)
    return parser.parse_args()


def analyze_files(files, display_lines, display_words,
                  display_bytes) -> (int, int, int):
    """Prints the count of lines, words and bytes in each of the files."""
    total_line_count = 0
    total_word_count = 0
    total_byte_count = 0

    for file in files:
        line_count = 0
        word_count = 0
        byte_count = 0

        for line in file:
            line_count += 1
            word_count += len(line.split())
            byte_count += len(line)
        output = f' {file.name}'
        if display_bytes:
            output = f'{byte_count:>8}' + output
        if display_words:
            output = f'{word_count:>8}' + output
        if display_lines:
            output = f'{line_count:>8}' + output
        print(output)

        total_line_count += line_count
        total_word_count += word_count
        total_byte_count += byte_count

    if len(files) > 1:
        output = ' total'
        if display_bytes:
            output = f'{total_byte_count:>8}' + output
        if display_words:
            output = f'{total_word_count:>8}' + output
        if display_lines:
            output = f'{total_line_count:>8}' + output
        print(output)


def main():
    """Get file names from the command line and print the count of their lines,
    words and bytes."""
    args = get_args()
    command = args.command
    files = args.files
    if command == 'cat':
        for file in files:
            print(file.read())
    elif command == 'head':
        length = args.characters
        for file in files:
            print(file.read()[:length])
    elif command == 'tail':
        length = args.characters
        for file in files:
            print(file.read()[-length + 1:])
    elif command == 'tac':
        for file in files:
            print(''.join(list(file)[::-1]))
    elif command == 'count':
        display_lines = args.lines
        display_words = args.words
        display_bytes = args.bytes
        if not any([display_lines, display_words, display_bytes]):
            display_lines = True
            display_words = True
            display_bytes = True
        analyze_files(files, display_lines, display_words, display_bytes)


if __name__ == '__main__':
    main()
