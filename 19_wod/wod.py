#!/usr/bin/env python
"""
Purpose: Create a random workout routine.
"""

import argparse
import csv
import random


def get_args():
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description='Creates a random workout routine.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='CSV file to read')
    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        default=None,
                        help='Random seed')
    parser.add_argument('-n',
                        '--num',
                        metavar='exercises',
                        type=int,
                        default=4,
                        help='Number of exercises')
    parser.add_argument('-e',
                        '--easy',
                        help='Half as many reps',
                        action='store_true',
                        default=False)
    args = parser.parse_args()
    if args.num <= 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def print_random_exercises(file, easy, number):
    """Print random exercises from the csv file based on he arguments
    provided."""
    reader = csv.reader(file)
    next(reader)
    data = random.sample(list(reader), k=number)
    exercises, reps = list(zip(*data))
    exercise_column_width = len(max(exercises, key=len))
    reps_column_width = 6
    print('Exercise'.ljust(exercise_column_width) + '  ' +
          'Reps'.rjust(reps_column_width))
    print('-' * exercise_column_width + '  ' + '-' * reps_column_width)
    for exercise, rep in zip(exercises, reps):
        rep = str(random.randint(*map(int, rep.split('-'))))
        if easy:
            rep = str(int(rep) // 2)
        print(exercise.ljust(exercise_column_width) + '  ' + rep.rjust(6))


def main():
    """Get command line arguments and print exercise schedule."""
    args = get_args()
    random.seed(args.seed)
    if args.file is None:
        args.file = open('inputs/exercises.csv')
    print_random_exercises(args.file, args.easy, args.num)


if __name__ == '__main__':
    main()
