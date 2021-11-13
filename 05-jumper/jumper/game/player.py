class Player:
    def __init__(self):
        pass

    def ask_letter():
        guess = input("Guess a letter [a-z]: ")
        return guess
    
    def guess_letter(self, lib):
        """
        Add the letter to the library
        """
        letter = (Player.ask_letter())
        letter.lower()
        while letter in lib:
            print("That letter was already chosen:")
            letter = (Player.ask_letter())
            letter.lower()
        lib.append(letter)
        return lib