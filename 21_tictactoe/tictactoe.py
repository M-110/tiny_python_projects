#!/usr/bin/env python
"""
Purpose: Play a round of tic-tac-toe.
"""

import argparse

BOARD = """
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------"""


def get_args():
    """Get arguments from command line."""
    parser = argparse.ArgumentParser(
        description='Play a round of tic-tac-toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b',
                        '--board',
                        type=str,
                        help='State of the board',
                        default='.........')
    parser.add_argument('-p',
                        '--player',
                        type=str,
                        choices=['X', 'O'],
                        help='Player\'s marker, X or O')
    parser.add_argument('-c',
                        '--cell',
                        type=int,
                        choices=list(range(1, 10)),
                        help='Player\'s marker, X or O')
    args = parser.parse_args()
    if bool(args.player) != bool(args.cell):
        parser.error('Must provide both --player and --cell')
    if args.cell and args.board[args.cell - 1] != '.':
        parser.error(f'--cell "{args.cell}" already taken')
    if len(args.board) != 9:
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')
    return parser.parse_args()


def is_winner(player, board):
    """Returns True if player has three marks in a row."""
    target = [player, player, player]
    winning_lines = (
        [board[i:i + 3] for i in range(0, 7, 3)] +
        [board[i:i + 7:3] for i in range(3)] +
        [[board[0], board[4], board[8]], [board[2], board[4], board[6]]])
    return any(line == target for line in winning_lines)


def main():
    """Get board state from command line and print a table representing the
    board."""
    args = get_args()
    board = list(args.board)
    player = args.player
    cell = args.cell
    if player:
        board[cell - 1] = player
    marks = [i if char == '.' else char for i, char in enumerate(board, 1)]
    print(BOARD.format(*marks))
    if is_winner('X', board):
        print('X has won!')
    elif is_winner('O', board):
        print('O has won!')
    else:
        print('No winner.')


if __name__ == '__main__':
    main()
