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
    return parser.parse_args()


def main():
    """Print a warning to the captain using the command line arguments."""
    name = get_args().name
    article = "an" if name[0].lower() in "aeiou" else "a"
    print(f"Ahoy, Captain, {article} {name} off the larboard bow!")


if __name__ == "__main__":
    main()
