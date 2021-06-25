#!/usr/bin/env python3
"""
Purpose: Capitalize the input of a command line argument. If it is a file then
the contents of the file will be capitalized. If flagged, it will output as a
new file.
"""
import argparse
import os


def get_args():
    """Get args from command line."""
    parser = argparse.ArgumentParser(
        description='Howler!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='Text or file to be capitalized')
    parser.add_argument('-l',
                        '--lower',
                        action='store_true',
                        help='Convert to lowercase')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output file',
                        default=None)
    parser.add_argument('-d',
                        '--outdir',
                        metavar='str',
                        type=str,
                        help='Output directory',
                        default=None)
    return parser.parse_args()


def read_file(file_name):
    """Read contents of file."""
    with open(file_name, encoding='utf8') as file:
        return file.read().rstrip().lstrip()


def write_file(file_name, text):
    """Write text to a file."""
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(text)


def copy_dir(from_dir, to_dir, lower):
    """Copy files from directory."""
    if not os.path.isdir(to_dir):
        os.mkdir(to_dir)
    for file_a in os.listdir(from_dir):
        with open(os.path.join(from_dir, file_a), encoding='utf8') as reader:
            with open(os.path.join(to_dir, file_a), 'w', encoding='utf8') as writer:
                text = reader.read().strip()
                if lower:
                    text = text.lower()
                else:
                    text = text.upper()
                writer.write(text)


def main():
    """Get args from command line and capitalize input."""
    args = get_args()
    text = args.text
    if args.outdir:
        copy_dir(text, args.outdir, args.lower)
    else:
        if '.txt' in text:
            text = read_file(text)
            
        if args.lower:
            text = text.lower()
        else:
            text = text.upper()
            
        if outfile := args.outfile:
            write_file(outfile, text)
        else:
            print(text)


if __name__ == '__main__':
    main()
