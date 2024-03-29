from __future__ import annotations
from typing import Dict, List, Optional
import dataclasses
import logging

from .scrabble import find_word, valid_start, construct_empty_board, calculate_points, difference
from fastapi import WebSocket
from ..game.tiles import TileManager


class InvalidWordException(Exception):
    """custom Exception class raised when the
    given word is invalid in Scrabble."""


class InvalidStartException(InvalidWordException):
    """an InvalidWordException raised specifically
    when the word placed is the first word of the game."""


class GameFull(Exception):
    """raised when a player tries to join a game that already has two players."""


class InvalidPerkException(Exception):
    """raised when a perk is activated when the player
    has exceeded the maximum number of times they're allowed to
    activate a perk"""


@dataclasses.dataclass
class Player:
    """dataclass to hold some attributes about each player in the lobby"""
    name: str
    socket: WebSocket
    points: int = 0
    tiles: List[str] = dataclasses.field(default_factory=list)
    numPerksAllowed: int = 3
    numPerksUsed: int = 0

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f'Player(name={self.name}, points={self.points})'

    def asdict(self) -> Dict[str, str]:
        return {'name': self.name, 'points': self.points, 'tiles': self.tiles}


class GameManager:
    """GameManager class takes care of all general game functions.
    The asdict function represents the entire game state, and should be sent to the client on every update"""
    def __init__(self, game_id: int, wordset: int = 1) -> None:
        self.id: int = game_id
        self.tileset = TileManager()
        # manage the players with an integer bounded to 0-1.
        self.current_player: int = 0
        self.turn: int = 0
        self.board = construct_empty_board()
        # a copy of the board from the previous turn, used to calculate the changes in the board state.
        self.old_board = self.board
        # the number of points each player has.
        self.game_running: bool = False
        self.winner: Optional[int] = None
        self._players: List[Optional[Player]] = [None, None]
        self.num_tiles: int = 7
        self.wordset = wordset

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
        self._players[player] = None

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

    def next_turn(self, board: List[List[str]], valid_words: list[str]) -> None:
        """advance the game state by a single turn, mutate the game board with the new word.
        this function will raise an InvalidGameStateException if the user places an invalid word.
        raising this exception will ensure that the board is not mutated in any way, and it will remain
        on the current player's turn."""
        logger = logging.getLogger("uvicorn.next_turn")
        # edge case that it's the first turn and the word placed isn't in the right place on the board
        if self.turn == 0:
            if not valid_start(board):
                logger.warning("invalid start")
                raise InvalidStartException()
        # find the word on the Scrabble board, and check if it's valid.
        word = find_word(self.old_board, board, self.turn)
        logger.info("%s placed", word)
        if not word:
            logger.warning("no word placed")
            raise InvalidWordException()
        if word.lower() not in valid_words:
            logger.warning("invalid word placed")
            raise InvalidWordException("invalid word placed")
        placed = difference(self.old_board, board)
        self.old_board = board
        self.board = board
        current_player = self.players[self.current_player]
        current_player.points += calculate_points(word)
        # if the player didn't place the letter (i.e. used a letter that was already on the board)
        # don't try and remove that letter from their tileset.
        for char in placed:
            for i, tile in enumerate(current_player.tiles):
                if tile[0] == char:
                    current_player.tiles.pop(i)
                    break
        # draw n number of tiles from the tileset so that len(current_player.tiles) == 7
        new_tiles = self.tileset.draw(self.num_tiles - len(current_player.tiles))
        current_player.tiles.extend(new_tiles)

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

    def extra_letter_perk(self, numLetters: int) -> None:
        """adds a specific no. of tiles to the players tileset, 
        each tile costs 2 points"""
        player = self._players[self.current_player]
        if player.points < 2 * numLetters:
            raise ValueError("Not enough points for the perk")
        elif player.numPerksUsed >= player.numPerksAllowed:
            raise ValueError("Not enough perks remaining")
        else:
            player.points -=  2 * numLetters
            player.numPerksUsed += 1
            new_tile = self.tileset.draw(numLetters)
            player.tiles.extend(new_tile)

    def change_letters_perk(self) -> None:
        player = self._players[self.current_player]
        if player.points < 3:
            raise ValueError("Not enough points for the perk")
        elif player.numPerksUsed >= player.numPerksAllowed:
            raise ValueError("Not enough perks remaining")
        else:
            player = self._players[self.current_player]
            player.numPerksUsed += 1
            player.points -= 3
            player.tiles = self.tileset.draw(self.num_tiles)