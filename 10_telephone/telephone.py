#!/usr/bin/env python3
"""
Purpose: Mutate the given text string with random changed letters.
"""

import argparse
import random
import string


def get_args():
    """Get args from the command line."""
    parser = argparse.ArgumentParser(
        description='Randomly mutate a given string',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                       type=str,
                       help='Text or file to be mutated',
                       default=None)
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        help='Random generator seed',
                        default=None)
    parser.add_argument('-m',
                        '--mutations',
                        type=float,
                        help='Mutation probability',
                        default=.1)
    args = parser.parse_args()
    mutations = args.mutations
    if not 0 <= mutations <= 1:
        parser.error(f'--mutations "{mutations}" must be between 0 and 1')
    return args


def main():
    """Print a randomly mutated string."""
    args = get_args()
    random.seed(args.seed)
    text = args.text
    if '.txt' in text:
        with open(text, encoding='utf8') as file:
            text = file.read().rstrip()

    mutations = args.mutations
    mutation_count = round(len(text) * mutations)

    char_count = len(text)
    characters = string.ascii_letters + string.punctuation

    new_text = list(text)

    for i, new_char in zip(random.sample(range(char_count), mutation_count),
                           random.choices(characters, k=mutation_count)):
        new_text[i] = new_char

    new_text = ''.join(new_text)

    print(f'You said: "{text}"')
    print(f'I heard : "{new_text}"')


if __name__ == '__main__':
    main()
