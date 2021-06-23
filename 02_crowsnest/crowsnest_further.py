#!/usr/bin/env python3
"""
Purpose: Describe what is off the larboard bow using the correct a/an article.
"""

import argparse


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Warn the captain",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("name", metavar="name", help="Name of the creature")
    parser.add_argument("--side",
                        metavar="side",
                        help="Side of the ship",
                        default='larboard')
    return parser.parse_args()


def main():
    """Print a warning to the captain using the command line arguments."""
    args = get_args()
    name = args.name
    side = args.side
    if not name[0].isalpha():
        raise ValueError("Name must begin with an alphabetical character.")
    article = "an" if name[0].lower() in "aeiou" else "a"
    if name.istitle():
        article = article.title()
    print(f"Ahoy, Captain, {article} {name} off the {side} bow!")


if __name__ == "__main__":
    main()
