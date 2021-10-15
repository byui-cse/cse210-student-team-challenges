from game.word_bank import Word_Bank


class Board:
    def __init__(self):
        self.word_bank = Word_Bank()

    def word_to_list(self):
        word = str(self.word_bank.get_random_word())
        list_of_letters = list(word)
        return list_of_letters

    def put_user_guess(self):
        user_guess = input("Make a guess: ")
