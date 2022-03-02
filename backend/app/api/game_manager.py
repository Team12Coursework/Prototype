from __future__ import annotations
from typing import Dict, List, MutableSet, Tuple, Optional
import random
import dataclasses

import numpy as np

from app.api.scrabble import find_word, valid_start, construct_empty_board, calculate_points
from fastapi import WebSocket


class InvalidWordException(Exception):
    """custom Exception class raised when the
    given word is invalid in Scrabble."""


class InvalidStartException(InvalidWordException):
    """an InvalidWordException raised specifically
    when the word placed is the first word of the game."""


class GameFull(Exception):
    """raised when a player tries to join a game that already has two players."""


@dataclasses.dataclass
class Player:
    """dataclass to hold some attributes about each player in the lobby"""
    name: str
    socket: WebSocket
    points: int = 0
    tiles: List[str] = dataclasses.field(default_factory=list)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Player(name={self.name}, points={self.points})'

    def asdict(self) -> Dict[str, str]:
        return {'name': self.name, 'points': self.points, 'tiles': self.tiles}


class TileManager:
    """tile manager class will manage the deck of tiles for the game to draw upon"""
    def __init__(self) -> TileManager:
        # dictionary holding the tile and the number of times the tile occurs
        self.tiles: Dict[str, int] = {
            'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6,
            'T': 6, 'L': 4,  'S': 4, 'U': 4, 'D': 4, 'G': 3,
            'B': 2, 'C': 2,  'M': 2, 'P': 2, 'F': 2, 'H': 2,
            'V': 2, 'W': 2,  'Y': 2, 'K': 1, 'J': 1, 'X': 1,
            'Q': 1, 'Z': 1,
        }
        self.remaining_tiles: List[str] = list(self.tiles.keys())

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
                self.remaining_tiles.remove(letter)
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
    """GameManager class takes care of all general game functions.
    The asdict function represents the entire game state, and should be sent to the client on every update"""
    def __init__(self, game_id: int) -> GameManager:
        self.id: int = game_id
        self.tileset = TileManager()
        # manage the players with an integer bounded to 0-1.
        self.current_player: int = 0
        self.turn: int = 0
        self.board: np.ndarray = construct_empty_board()
        # a copy of the board from the previous turn, used to calculate the changes in the board state.
        self.old_board: np.ndarray = self.board
        # the number of points each player has.
        self.game_running: bool = False
        self.winner: Optional[int] = None
        self._players: List[Optional[Player]] = [None, None]
        self.num_tiles: int = 7

    @property
    def full(self) -> bool:
        return len(self.players) == 2

    @property
    def players(self) -> List[Player]:
        return list(filter(lambda x: x is not None, self._players))

    def add_player(self, player: Player) -> None:
        """function to add a player to the game, not a fantastic way of doing this
        but there are only ever two players so not too bad :)"""
        if self._players[0] is None:
            self._players[0] = player
        elif self._players[1] is None:
            self._players[1] = player
        else:
            raise GameFull()

    def forfeit(self, player: int) -> None:
        """forfeit the game and set the winner to the other player"""
        self.game_running = False
        self.winner = 1-player

    def advance_turn(self) -> None:
        """advance the game state by a single turn, this can be called directly if
        the turn is skipped, otherwise it's called implicitly by the next_turn() function"""
        self.next_player()
        self.turn += 1

    def reset(self) -> None:
        """reset the game state to a fresh game. Also used to start games
        function requires all players to be in the game"""
        if not self.full:
            raise InvalidStartException('cannot start the game with a single player in the lobby')
        self.board = construct_empty_board()
        for player in self.players:
            player.tiles = self.tileset.draw(self.num_tiles)
        self.game_running = True

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
        word: str = find_word(self.old_board, board, self.turn)
        if not word:
            raise InvalidWordException()
        self.old_board = board
        self.board = board
        current_player = self.players[self.current_player]
        current_player.points += calculate_points(word)
        # draw n number of tiles from the tileset so that len(current_player.tiles) == 7
        new_tiles = self.tileset.draw(self.num_tiles - len(current_player.tiles))
        current_player.tiles.append(new_tiles)

        self.advance_turn()

    def next_player(self) -> int:
        """toggle the value of current_player between 0 and 1, returns the new value of current_player."""
        self.current_player = 1 - self.current_player
        return self.current_player

    def asdict(self) -> Dict[str, str]:
        return {
            'type':             'gameUpdate',
            'turn':             self.turn,
            'currentPlayer':    self.current_player,
            'players':          [player.asdict() for player in self.players],
            'board':            self.board,
            'gameRunning':      self.game_running,
            'winner':           self.winner,
        }

    def one_random_letter(self, player : Player) -> None:
        player.points -=  2
        new_tile = self.tileset.draw(1)
        player.tiles.append(new_tile)

    def two_random_letters(self, player : Player) -> None:
        player.points -= 4
        new_tiles = self.tileset.draw(2)
        player.tiles.append(new_tiles)

    def change_letters_available(self , player: Player) -> None:
        player.points -= 3
        player.tiles = self.tileset.draw(self.num_tiles)
        