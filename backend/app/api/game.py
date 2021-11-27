from fastapi import APIRouter
import json
import random

router = APIRouter()

"""
file holds all of the routes for the game behaviour
"""


points = {
    "A": 1, "B": 4, "C": 1, "D": 2, "E": 1, "F": 3, "G": 2, "H": 3, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1,
    "O": 1, "P": 4, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 2, "V": 5, "W": 5, "X": 10, "Y": 4, "Z": 8
}


# 12 E's, 10 A's, 8 R's , 8 I's, 7 N's, 6 L's, 6 O's, 5 T's, 5 S's, 3 C's, 3 U's, 3 G's, 3 D's, 3 H's, 2 F's, 2 M's, 2 Y's, 2 P's,
# 2 B's, 2 V's, 1 k, 1 W, 1 Z, 1 J, 1 X, 1 Q
tiles = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "R", "R", "R", "R", "R",
         "R", "R", "R", "I", "I", "I", "I", "I", "I", "I", "I", "N", "N", "N", "N", "N", "N", "N", "L", "L", "L", "L", "L", "L", "O", "O", "O",
         "O", "O", "O", "T", "T", "T", "T", "T", "S", "S", "S", "S", "S", "C", "C", "C", "U", "U", "U", "G", "G", "G", "D", "D", "D", "H", "H",
         "H", "F", "F", "M", "M", "Y", "Y", "P", "P", "B", "B", "V", "V", "K", "W", "Z", "J", "X", "Q"]


# For keeping track of the number of turns
num_turn = 2


# If the search word returns a valid word, find its points and add it to the total
# Otherwise return an exception
def validate_Word():
    word = find_Word(array1, array2)

    if valid_start(array2) and len(word) > 0:
        word_points = calculate_Points(word)
        print(word)
        print(word_points)
        # Update the players score in the database
        return True
    else:
        print("No word")
        return False


# Will search the array for the word and the Database to see if it exists
def find_Word(arr1, arr2):
    word = ""

    x = 0
    y = 0

    # For checking if the word is connected to another word
    check1 = 0
    check2 = 0

    for i in range(x, 15):
        for j in range(0, 16):
            if j:  # If J is not none
                if arr1[x][y] != arr2[x][y]:  # If the original old array does not contain the letter
                    y2 = y

                    if y2 < 14 and arr2[x][y2+1]:
                        while arr2[x][y2-1]:  # It will find where the word starts
                            y2 = y2-1
                        while arr2[x][y2]:  # It will start adding the letters to the word, from where it starts
                            if x < 15 and y2 < 15:
                                word += arr2[x][y2]


                            # For checking if the word is connected to another word
                            if num_turn > 0:
                                if 0 <= x < 14 and arr2[x + 1][y2] or arr2[x - 1][y2]:
                                    check1 = check1 + 1

                            y2 = y2 + 1
                            if y2 == 15:
                                break


                    x2 = x
                    if x2 < 14 and arr2[x2+1][y]:
                        while arr2[x2-1][y]:
                            x2 = x2-1
                        while arr2[x2][y]:
                            if x2 < 15 and y < 15:
                                word += arr2[x2][y]

                            # For checking if the word is connected to another word
                            if num_turn > 0:
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
    elif num_turn > 0 and check1 == 0 and check2 == 0:
        return ""
    else:
        # For now it searches the JSON file
        f = open('words_dictionary.json')

        data = json.load(f)

        for i in data:
            if str(i).upper() == word:
                return word

    return ""



# Checks if the start of the game is valid
# The first letter must be placed in the middle of the board ([7][7])
# The rest of the letters must be placed across or down from the center
def valid_start(arr):
    valid = False

    if num_turn == 0 and arr[7][7]:
        if arr[6][7] is None and arr[7][6] is None:
            valid = True
    elif num_turn > 0:
        valid = True

    return valid


def calculate_Points(word):
    total_points = 0

    for letter in word:
        total_points += points[letter]

    return total_points


# Gets a random tile from the tiles list
def get_Tile():
    index = random.randint(0, len(tiles))
    tile = tiles[index]
    tiles.pop(index)  # Removes the tile from the list

    return tile
