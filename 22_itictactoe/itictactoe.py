#!/usr/bin/env python
"""
Purpose: Play an interactive game of tic tac toe.
"""
from dataclasses import dataclass, field
import sys
from typing import Literal, Optional

BOARD = """
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------
| {} | {} | {} |
-------------"""


@dataclass
class State:
    """Current state of a tic-tac-toe game."""
    board: list[str] = field(default_factory=lambda: ['.'] * 9)
    player: Literal['X', 'O'] = 'X'
    quit: bool = False
    draw: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


def main():
    """Run the game."""
    state = State()
    while not (state.winner or state.draw):
        move = get_player_move(state)
        state.board[move] = state.player
        check_for_game_over(state)
        next_player_turn(state)
    print_board(state)


def get_player_move(state: State) -> int:
    """Get the index of the square the player wants to select."""
    print_board(state)
    player = state.player
    move = input(f'Player {player}, what is your move? [q to quit]: ')
    if move in list(map(str, range(1, 10))):
        if state.board[int(move) - 1] != '.':
            state.error = f'Cell "{move}" already taken'
        else:
            state.error = None
            return int(move) - 1
    if move == 'q':
        sys.exit()
    elif move not in list(map(str, range(1, 10))):
        state.error = f'Invalid cell "{move}", please use 1-9'
    return get_player_move(state)


def print_board(state: State) -> None:
    """Print the current state of the board and the error if one exists."""

    marks = [
        i if char == '.' else char for i, char in enumerate(state.board, 1)
    ]
    print(BOARD.format(*marks))
    if state.error:
        print(state.error)
    if state.winner:
        print(f'{state.winner} has won!')
    if state.draw:
        print('Draw!')


def check_for_game_over(state) -> None:
    """Updates the winner or draw attribute of the state if the game has
    ended."""
    board = state.board
    winning_lines = (
        [board[i:i + 3] for i in range(0, 7, 3)] +
        [board[i:i + 7:3] for i in range(3)] +
        [[board[0], board[4], board[8]], [board[2], board[4], board[6]]])
    if any(line == ['X', 'X', 'X'] for line in winning_lines):
        state.winner = 'X'
    elif any(line == ['O', 'O', 'O'] for line in winning_lines):
        state.winner = 'O'
    elif '.' not in board:
        state.draw = True


def next_player_turn(state):
    """Set the player state to the next player."""
    state.player = 'X' if state.player == 'O' else 'O'


if __name__ == '__main__':
    main()
