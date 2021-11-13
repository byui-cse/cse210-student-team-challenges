
class Board:
    def __init__(self, p1, p2, g1, g2, h1, h2):
        self._player1 = p1
        self._player2 = p2
        self._guess1 = g1
        self._guess2 = g2
        self._hint1 = h1
        self._hint2 = h2

    def print(self):
        hint1 = "".join(self._hint1)
        hint2 = "".join(self._hint2)
        print("--------------------")
        print("Player {0}: {1}, {2}".format(self._player1, self._guess1, hint1))
        print("Player {0}: {1}, {2}".format(self._player2, self._guess2, hint2))
        print("--------------------")