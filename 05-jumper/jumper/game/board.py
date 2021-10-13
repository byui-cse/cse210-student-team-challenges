# from game.guess import guess
# from game.word import word

class Board:
    def __init__(self):
        self.secret_word = []
        self.jumper_state = 5  # jumper state initilizes at full health
        self.jumper_display = [("  ___  "), (" /___\ "), (" \   / "), ("  \ /  "),
                               ("   0   "), ("  /|\  "), ("  / \  "), ("       "), ("^^^^^^^")]
        # update array indexes 0,1,2,3,4 for drop in health

    def display(self):
        for line in self.jumper_display:
            print(line)

    def update_secret(self):
        pass

    def get_hint(self):
        pass


board = Board()
board.display()
