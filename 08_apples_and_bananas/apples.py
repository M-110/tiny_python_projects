#!/usr/bin/env python3
"""
Purpose: Replace the letter a in the given text with a given vowel.
"""
import argparse
import re


def get_args():
    """Get arguments from the command line."""
    parser = argparse.ArgumentParser(
        description='Replace text with given vowel.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='str',
                        help='Text or file to be converted',
                        type=str)
    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to replace',
                        default='a',
                        type=str,
                        choices=['a', 'e', 'i', 'o', 'u'])
    parser.add_argument('-c',
                        '--collapse',
                        help='Combine consecutive vowels',
                        action='store_true')
    args = parser.parse_args()
    return args


def main():
    """Print converted sentence with the new vowels."""
    args = get_args()
    new_vowel = args.vowel
    text = args.text
    
    if '.txt' in text:
        with open(text, encoding='utf8') as file:
            text = file.read()
            
    pattern = '[aeiou]'
    if args.collapse:
        pattern += '+'
        
    text = re.sub(pattern, new_vowel, text)
    text = re.sub(pattern.upper(), new_vowel.upper(), text)
        
    print(text)


if __name__ == '__main__':
    main()
