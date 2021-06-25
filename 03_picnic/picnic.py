#!/usr/bin/env python3
"""
Purpose: Print a list of what you're bringing to the picnic.
"""

import argparse
import sys


def get_args():
    """Get args from the command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument('items',
                        type=str,
                        help='Item(s) to bring to the picnic',
                        nargs='+')
    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the list alphabetically',
                        action='store_true')
    parser.add_argument('-n',
                        '--noxford',
                        help='Do not include an oxford comma',
                        action='store_true')
    parser.add_argument('--separator',
                        metavar='separator',
                        help='Include a custom separator',
                        default=',')
    args = parser.parse_args()
    if len(args.items) == 0:
        print(str(parser.usage))
        sys.exit()
    return args


def main():
    """Print what you are bringing to the picnic."""
    args = get_args()
    items = args.items

    sep = args.separator
    no_oxford = args.noxford
    if args.sorted:
        items.sort()
    if len(items) == 1:
        items = items[0]
    elif len(items) == 2:
        items = ' and '.join(items)
    else:
        items = f'{sep} '.join(
            items[:-1]) + f'{"" if no_oxford else sep} and ' + items[-1]
    print(f'You are bringing {items}.')


if __name__ == '__main__':
    main()
