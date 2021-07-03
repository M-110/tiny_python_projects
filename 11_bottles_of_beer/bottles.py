#!/usr/bin/env python3
"""
Purpose: Count down the numbers of bottles on the wall.
"""

import argparse
from typing import List, Union

from num2words import num2words

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
    parser.add_argument('-s',
                        '--steps',
                        help='How many steps to take',
                        default=1,
                        type=int)
    parser.add_argument('-t',
                        '--text',
                        help='Print numbers as text',
                        action='store_true')
    parser.add_argument('-r',
                        '--reversed',
                        help='Reverse the order',
                        action='store_true')

    args = parser.parse_args()
    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')
    if args.steps < 1:
        parser.error(f'--steps "{args.steps}" must be greater than 0')
    return args


def generate_sequence(number: int, steps: int, reverse: bool) -> List[int]:
    """Generate a  bottle sequence which will count bottles a number of times
    with the given step length."""
    if reverse:
        return [min(i, number) for i in range(0, number + steps, steps)]
    else:
        return [max(i, 0) for i in range(number, -steps, -steps)]


def print_sequence(sequence: List[int], text: bool):
    """Convert."""
    length = len(sequence) - 1
    for i in range(length):
        current_number = sequence[i]
        next_number = sequence[i + 1]
        step = num2words(abs(current_number - next_number))

        current_plural = pluralize(current_number)
        next_plural = pluralize(next_number)

        step_pronoun = 'it' if step == 'one' else 'them'

        if text:
            current_number = num2words(current_number).title()
            next_number = num2words(next_number).title()
            
        if next_number in ['Zero', 0]:
            next_number = 'No more'

        line_end = '' if i == length - 1 else '\n'
        print_verse(current_number, current_plural, next_number,
                    next_plural, step, step_pronoun, line_end)


def pluralize(number: int):
    """Returns 's' if the number is not 1, otherwise returns ''."""
    if number == 1:
        return ''
    else:
        return 's'


def print_verse(current_number: Union[str, int], current_plural: Union[str, int], next_number: str,
                next_plural: str, step: str, step_pronoun: str,
                line_end: str):
    """Print a verse of the song given the string parameters."""
    print(f'''{current_number} bottle{current_plural} of beer on the wall,
{current_number} bottle{current_plural} of beer,
Take {step} down, pass {step_pronoun} around,
{next_number} bottle{next_plural} of beer on the wall!{line_end}''')


def main():
    args = get_args()
    sequence = generate_sequence(args.number, args.steps, args.reversed)
    print_sequence(sequence, args.text)


if __name__ == '__main__':
    main()
