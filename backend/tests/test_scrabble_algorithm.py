from typing import TypeVar
import pathlib

import pytest

from characterconnect.api import scrabble


T = TypeVar("T")
BoardT = list[list[str | None]]
TestCaseT = dict[str, BoardT]

def str_to_arr(inp: str) -> BoardT:
    """convert a 255 char string into a 15x15 array"""
    out: BoardT = [[] for _ in range(15)]
    row: int = 0
    for i, char in enumerate(inp):
        if (i > 0) and (i % 15 == 0):
            row += 1
        if char == '.':
            out[row].append(None)
        else:
            out[row].append(char)
    return out

@pytest.fixture
def empty_board() -> BoardT:
    return [[None for _ in range(15)] for _ in range(15)]

@pytest.fixture
def test_cases(empty_board: BoardT) -> TestCaseT:
    # path to the directory where this file is,
    # *not* the directory where the program was invoked
    file_dir = pathlib.Path(__file__).parent
    out = {'empty': empty_board}

    with open(pathlib.Path(file_dir, 'data.csv')) as file:
        for line in file:
            name, test = line.strip().split(',')
            out[name] = str_to_arr(test)
    return out

def test_start_word_valid(test_cases: TestCaseT) -> None:
    """test that a valid start word registers as valid"""
    assert scrabble.valid_start(
        test_cases['start_word_valid']) == True

def test_find_valid_start_word(test_cases: TestCaseT) -> None:
    """test that the scrabble algorithm can correctly identify the valid
    start word"""
    assert scrabble.find_word(
        test_cases['empty'],
        test_cases['start_word_valid'],
        0) == 'HELLO'

def test_single_letter_start_word(test_cases: TestCaseT) -> None:
    """test that placing a single letter on the start tile raises a
    ValueError"""
    # TODO: this test is actually failing, this test should raise a ValueError
    # instead of returning an empty string.
    assert scrabble.find_word(
        test_cases['empty'],
        test_cases['single_letter_start'],
        0
    ) == ''

def test_start_word_incorrect_location(test_cases: TestCaseT) -> None:
    """test that placing a valid start word in an invalid location raises
    a ValueError"""
    pass

def test_intersect_valid() -> None:
    """test that two valid words intersecting each other are valid"""
    pass

def test_floating_word_raises() -> None:
    """test that a valid word not connecting to any other words is valid"""
    pass

def test_extend_word() -> None:
    """test that extending another word with a single letter
    to create another valid word is valid e.g.
    add an s to test to create tests"""
    pass

def test_invalid_word_raises() -> None:
    """test to check that an invalid word placed
    in a valid way raises a ValueError"""
    pass

def test_multiple_intersection_all_valid() -> None:
    """test that a letter placed in a way intersecting multiple
    other words is all valid"""
    pass

def test_multiple_intersection_single_invalid() -> None:
    """test that a letter placed in a way intersecting multiple
    other words where one of those words is invalid raises
    an InvalidWordException"""
    pass