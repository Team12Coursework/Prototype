import random

points = {
    "A": 1, "B": 4, "C": 1, "D": 2, "E": 1, 
    "F": 3, "G": 2, "H": 3, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1,
    "P": 4, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 2, "V": 5, "W": 5, "X": 10, "Y": 4, "Z": 8
}

class TileManager:
    """tile manager class will manage the deck of tiles for the game to draw upon"""
    def __init__(self) -> None:
        # you may be wondering why we"re not using a dict here. Dictionaries and Sets in Python are technically sorted on insertion order since 3.6
        # so it would probably be fine to get the set of keys and convert it into a list to get the letters out, but it seems like a faulty abstraction to me.
        # I"d rather have two arrays as needed, then you can pass the population (letters), and weights (number of letters in the bag)
        # directly into the random function and get the letters out. If you really need a dict for debugging or something, you can use
        # dict(zip(self._letters, self._weights)).

        # Scrabble tile letter distribution is as follows: 
        # A-9, B-2, C-2, D-4, E-12, F-2, G-3, H-2, I-9, J-1, K-1, L-4, M-2, N-6, O-8, P-2, Q-1, R-6, S-4, T-6, U-4, V-2, W-2, X-1, Y-2, Z-1 and Blanks-2.
        self.generator = random.Random()
        self._letters = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self._weights = [
            9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 
            6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1]
        # letter_id is used to uniquely identify the letter to prompt the frontend
        # to rerender. If this is not included, the frontend won't notice a change
        # if you draw the same letter twice in a row, and it won't render properly.
        # The player effectively loses a letter.
        self._letter_id = 0

    def draw(self, k: int, /) -> list[tuple[str, int, int]]:
        """draw n tiles from the available tileset and return the letters"""
        letters = self.generator.sample(self._letters, counts=self._weights, k=k)
        # Since our letters are all uppercase ASCII chars, the index of the letter in the array
        # is always 65 - ord(letter). This loop is used to remove the letters that were drawn
        # from the tileset.
        out: list[tuple[str, int, int]] = []
        for letter in letters:
            idx = 65 - ord(letter)
            self._weights[idx] -= 1
            out.append((letter, points[letter], self._letter_id))
            self._letter_id += 1
        return out


class TestManager(TileManager):
    """tile manager class used in the unit tests to create a pre-determined draw"""

    def __init__(self) -> None:
        super().__init__()
        # randomly generated seed from here:
        # https://www.uuidgenerator.net/version1
        # could be anything, needs to be kept the same otherwise all our unit tests will fail :)
        self.seed = "f0867a2c-ff00-43b9-800b-ea6eb17b980f"
        self.generator = random.Random(self.seed)