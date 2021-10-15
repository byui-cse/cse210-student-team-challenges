from game.board import Board
from game.word_bank import Word_Bank


class Director:
    def __init__(self):

        self.play_again = True
        self.board = Board()

    def start_game(self):

        while self.play_again:
            self.get_inputs()
            self.board.put_user_guess()

    def get_inputs(self):

        self.board.word_to_list()

        again = input("Do you want to play again? [y/n] :")
        if again.lower() == 'y':
            self.play_again = True
        elif again.lower() == 'n':
            self.play_again = False
        else:
            again = (
                "That is not a valid input. Please enter 'y' for yes and 'n' for no")
