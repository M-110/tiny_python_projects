#!/usr/bin/env python
"""
Purpose: Generate a random password.
"""

import argparse
import random
import re

LEET_DICT = dict(a='@', A='4', O='0', t='t', E='3', I='1', S='5')


def get_args():
    parser = argparse.ArgumentParser(
        description='Random password generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='*',
                        help='Files to retrieve words from')
    parser.add_argument('-n',
                        '--num',
                        metavar='num_passwords',
                        type=int,
                        default=3,
                        help='Number of passwords to create')
    parser.add_argument('-w',
                        '--num_words',
                        type=int,
                        default=4,
                        help='Number of words to use per password')
    parser.add_argument('-m',
                        '--min_word_len',
                        metavar='minimum',
                        type=int,
                        default=3,
                        help='Minimum word length')
    parser.add_argument('-x',
                        '--max_word_len',
                        metavar='maximum',
                        default=6,
                        type=int,
                        help='Maximum word length')
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        default=None,
                        help='Random seed')
    parser.add_argument('-l',
                        '--l33t',
                        default=False,
                        action='store_true',
                        help='Obfuscate letters')
    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    if args.num_words < 1:
        parser.error(f'--num_words "{args.num_words}" must be greater than 0')
    if args.min_word_len < 1:
        parser.error(f'--min_word_len "{args.min_word_len}" must be greater '
                     f'than 0')
    if args.max_word_len < 1:
        parser.error(f'--max_word_len "{args.max_word_len}" must be greater '
                     f'than 0')
    if args.max_word_len < args.min_word_len:
        parser.error(f'--max_word_len "{args.max_word_len}" must be greater '
                     f'than or equal to --min_word_len "{args.min_word_len}"')
    return args


def get_words(files, min_word_len, max_word_len):
    return sorted({
        word.title()
        for file in files
        for word in map(lambda x: re.sub('\W', '', x),
                        file.read().splitlines())
        if min_word_len <= len(word) <= max_word_len
    })


def generate_n_passwords(words, num_passwords, num_words, leet):
    return [
        generate_password(words, num_words, leet) for _ in range(num_passwords)
    ]


def generate_password(words, num_words, leet):
    """Generate a password with random words and optionally convert to l33t
    speak."""
    password = ''.join(random.sample(words, k=num_words))
    if leet:
        password = leet_translate(password)
    return password


def leet_translate(password):
    for letter, leet_letter in LEET_DICT.items():
        password = password.replace(letter, leet_letter)
    return password


def main():
    """Get args and generate passwords."""
    args = get_args()
    random.seed(args.seed)
    words = get_words(args.files, args.min_word_len, args.max_word_len)
    passwords = generate_n_passwords(words, args.num, args.num_words, args.l33t)

    for password in passwords:
        print(password)


if __name__ == '__main__':
    main()
