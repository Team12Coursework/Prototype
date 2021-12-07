from __future__ import annotations
from typing import Dict, List, MutableSet, Tuple
import random

import numpy as np

from app.api.scrabble import find_word, valid_start, construct_empty_board, calculate_points


class InvalidWordException(Exception):
    """custom Exception class raised when the
    given word is invalid in Scrabble."""


class InvalidStartException(InvalidWordException):
    """an InvalidWordException raised specifically
    when the word placed is the first word of the game."""


class TileManager:
    """tile manager class will manage the deck of tiles for the game to draw upon"""
    def __init__(self) -> TileManager:
        # dictionary holding the tile and the number of times the tile occurs
        self.tiles: Dict[str, int] = {
            'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6,
            'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3,
            'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2,
            'V': 2, 'W': 2, 'Y': 2, 'K': 1, 'J': 1, 'X': 1,
            'Q': 1, 'Z': 1,
        }
        self.remaining_tiles: MutableSet[str] = set(self.tiles.keys())

    def draw(self, n: int) -> List[str]:
        """draw n tiles from the available tileset"""
        if len(self.remaining_tiles) < n:
            raise IndexError(f'cannot remove {n} tiles from tileset, only {len(self.remaining_tiles)} tiles remaining')
        letters: List[str] = []
        for _ in range(n):
            letter: str = random.choice(self.remaining_tiles)
            if self.tiles[letter] >= 1:
                self.tiles[letter] -= 1
            else:
                self.remaining_tiles.pop(letter)
            letters.append(letter)
        return letters

    def draw_remaining(self) -> List[str]:
        """draws the remaining tiles from the deck"""
        letters: List[str] = []
        for letter, num_remaining in self.tiles.items():
            if num_remaining == 0:
                continue
            letters.append([letter] * num_remaining)
        return letters


class GameManager:
    """GameManager class takes care of all general game functions."""
    def __init__(self) -> GameManager:
        self.tileset = TileManager()
        # manage the players with an integer bounded to 0-1.
        self.current_player: int = 0
        self.turn: int = 0
        self.board: np.ndarray = construct_empty_board()
        # a copy of the board from the previous turn, used to calculate the changes in the board state.
        self.old_board: np.ndarray = self.board
        # the number of points each player has.
        self.points: Tuple[int, int] = (0, 0)

    def advance_turn(self) -> None:
        """advance the game state by a single turn, this can be called directly if
        the turn is skipped, otherwise it's called implicitly by the next_turn() function"""
        self.next_player()
        self.turn += 1

    def next_turn(self, board: List[List[str]]) -> int:
        """advance the game state by a single turn, mutate the game board with the new word.
        this function will raise an InvalidGameStateException if the user places an invalid word.
        raising this exception will ensure that the board is not mutated in any way, and it will remain
        on the current player's turn."""
        # edge case that it's the first turn and the word placed isn't in the right place on the board
        if self.turn == 0:
            if not valid_start(board):
                raise InvalidStartException()
        # find the word on the Scrabble board, and check if it's valid.
        word: str = find_word(self.old_board, board)
        if not word:
            raise InvalidWordException()
        self.old_board = board
        self.board = board
        self.points[self.current_player] += calculate_points(word)
        self.advance_turn()

    def next_player(self) -> int:
        """toggle the value of current_player between 0 and 1, returns the new value of current_player."""
        self.current_player = 1 - self.current_player
        return self.current_player