#!/usr/bin/env python3
"""
Purpose: Encrypt a number using the jump 5 algorithm.
"""

import argparse

JUMP_5_DICT = {1: 9, 2: 8, 3: 7, 4: 6, 5: 0, 0: 5, 6: 4, 7: 3, 8: 2, 9: 1}
INT_STRING_DICT = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero",
}


def get_args():
    """Get args from command line."""
    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text",
                        metavar="str",
                        help="Text to encrypt numbers from")
    parser.add_argument("-v",
                        "--verbose",
                        action="store_true",
                        help="convert numbers to strings")
    args = parser.parse_args()
    return args


def jump_5_encrypt(text: str, verbose: bool) -> str:
    """Encrypt all numbers within the text"""
    output = ""
    for char in text:
        if char.isnumeric():
            char = JUMP_5_DICT[int(char)]
            if verbose:
                output += INT_STRING_DICT[char]
            else:
                output += str(char)
        else:
            output += char
    return output


def main():
    """Get text from the command line and encrypt the numbers and print the
    result."""
    args = get_args()
    text = args.text
    verbose = args.verbose
    encrypted_text = jump_5_encrypt(text, verbose)
    print(encrypted_text)


if __name__ == "__main__":
    main()
