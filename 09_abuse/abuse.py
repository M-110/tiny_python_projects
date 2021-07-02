#!/usr/bin/env python3
"""
Purpose:
"""

import argparse
import random

NOUNS = [
    'Judas', 'Satan', 'ape', '***', 'barbermonger', 'beggar', 'block', 'boy',
    'braggart', 'butt', 'carbuncle', 'coward', 'coxcomb', 'cur', 'dandy',
    'degenerate', 'fiend', 'fishmonger', 'fool', 'gull', 'harpy', 'jack',
    'jolthead', 'knave', 'liar', 'lunatic', 'maw', 'milksop', 'minion',
    'ratcatcher', 'recreant', 'rogue', 'scold', 'slave', 'swine', 'traitor',
    'varlet', 'villain', 'worm'
]
ADJECTIVES = [
    'bankrupt', 'base', 'caterwauling', 'corrupt', 'cullionly', 'detestable',
    'dishonest', 'false', 'filthsome', 'filthy', 'foolish', 'foul', 'gross',
    'heedless', 'indistinguishable', 'infected', 'insatiate', 'irksome',
    'lascivious', 'lecherous', 'loathsome', 'lubbery', 'old', 'peevish',
    'rascaly', 'rotten', 'ruinous', 'scurilous', 'scurvy', 'slanderous',
    'sodden-witted', 'thin-faced', 'toad-spotted', 'unmannered', 'vile',
    'wall-eyed'
]


def get_args():
    """Get arguments from command line"""
    parser = argparse.ArgumentParser(
        description='Insult yourself',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        type=int,
                        help='Number of adjectives',
                        default=2)
    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type=int,
                        help='Number of insults',
                        default=3)
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        type=int,
                        help='Random seed',
                        default=None)
    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    elif args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


def main():
    """Print random insults."""
    args = get_args()
    random.seed(args.seed)

    for _ in range(args.number):
        adjectives = ', '.join(random.sample(ADJECTIVES, k=args.adjectives))
        noun = random.choice(NOUNS)
        print(f'You {adjectives} {noun}!')


if __name__ == '__main__':
    main()
