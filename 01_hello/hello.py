#!/usr/bin/env python3
"""Gets a name from the command line and says hello to the name."""

import argparse


def get_args():
    """Get args from the command line."""
    parser = argparse.ArgumentParser(description="Say Hello!")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """Get args from command line and print them."""
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
