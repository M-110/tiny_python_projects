#!/usr/bin/env python
"""
Purpose: Create a list of rhyming words.
"""

import argparse
import re
from typing import Tuple, Optional

STEMS = sorted(('bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st '
                'sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr '
                'b c d f g h j k l m n p q r s t v w x y z').split())


def get_args():
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description='Get a list of rhyming words.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('word', help='Word to be rhymed')
    return parser.parse_args()


def get_stems(word: str) -> Optional[Tuple[str, str]]:
    """Split the word by the first vowel"""
    pattern = '([^aeiou]*?)([aeoiu].*)'
    return re.findall(pattern, word.lower())[0]


def main():
    """Get the word and print the rhyming words."""
    args = get_args()
    word = args.word
    
    try:
        start, end = get_stems(word)
    except IndexError:
        print(f'Cannot rhyme "{word}"')
    else:
        for stem in STEMS:
            if stem == start:
                continue
            print(f'{stem}{end}')


if __name__ == '__main__':
    main()
