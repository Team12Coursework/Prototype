from typing import Dict, Optional, List

points: Dict[str, int] = {
    'A': 1, 'B': 4, 'C': 1, 'D': 2, 'E': 1, 'F': 3, 'G': 2, 'H': 3, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
    'O': 1, 'P': 4, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 5, 'W': 5, 'X': 10, 'Y': 4, 'Z': 8
}

BoardT = list[list[str | None]]

def construct_empty_board() -> List[List[Optional[str]]]:
    """construct a 15x15 NumPy array to represent the board"""
    return [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None] for _ in range(15)]

def calculate_points(word: str) -> int:
    """return the number of points the given word is worth"""
    return sum(points[char] for char in word)

def find_word(arr1, arr2, turn: int):
    """will search the array for the word and the Database to see if it exists"""

    word: str = ''

    x: int = 0
    y: int = 0

    # For checking if the word is connected to another word
    check1 = 0
    check2 = 0

    for i in range(x, 15):
        for j in range(0, 16):
            if j is not None:
                if arr1[x][y] != arr2[x][y]:  # If the original old array does not contain the letter
                    y2 = y

                    if y2 < 14 and arr2[x][y2 + 1]:
                        while arr2[x][y2 - 1]:  # It will find where the word starts
                            y2 = y2 - 1
                        while arr2[x][y2]:  # It will start adding the letters to the word, from where it starts
                            if x < 15 and y2 < 15:
                                word += arr2[x][y2]

                            # For checking if the word is connected to another word
                            if turn > 0:
                                if 0 <= x < 14 and arr2[x + 1][y2] or arr2[x - 1][y2]:
                                    check1 = check1 + 1

                            y2 = y2 + 1
                            if y2 == 15:
                                break
                    x2 = x
                    if x2 < 14 and arr2[x2 + 1][y]:
                        while arr2[x2 - 1][y]:
                            x2 = x2 - 1
                        while arr2[x2][y]:
                            if x2 < 15 and y < 15:
                                word += arr2[x2][y]

                            # For checking if the word is connected to another word
                            if turn > 0:
                                if 0 <= y < 14 and arr2[x2][y + 1] or arr2[x2][y - 1]:
                                    check2 = check2 + 1
                            x2 = x2 + 1
                            if x2 == 15:
                                break
            if len(word) == 0:
                y += 1
                if y == 15:
                    y = 0
            else:
                break
        if len(word) == 0:
            x += 1
            y = 0
        else:
            break
    if len(word) == 0:
        return ""
    elif (turn > 0) and (check1 == 0) and (check2 == 0):
        return ""
    return word


def valid_start(board) -> bool:
    """checks if the start of the game is valid the first letter
    must be placed in the middle of the board (7, 7)"""

    return board[7][7]