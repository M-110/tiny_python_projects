#!/usr/bin/env python3
"""
Purpose: Look up lines within a text file which begin with the letter passed
into the command.
"""


def main():
    """Print the lines which begin with the letter given by the command line
     argument"""
    with open('gashlycrumb.txt', encoding='utf8') as file:line_dict = {line[0].upper(): line for line in file}
    while (letter := input('Letter to lookup ("quit" to quit): ')) != 'quit':
        print(line_dict.get(letter.upper(), f'I do not know "{letter}".').rstrip())


if __name__ == '__main__':
    main()
