from game.console import Console
from game.word_bank import Word_Bank
from game.player import Player
from game.game_master import Game_Master
from game.parachute_man import Parachute_man

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.word_bank = Word_Bank()
        self.keep_playing = True
        self.player = Player()
        self.game_master = Game_Master()
        self.p_man = Parachute_man()
        self.player_letter = []
        self.lives = 0
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        word = self.word_bank.get_word()
        blank = self.word_bank.underscore(word)
       
        print(blank)
        print(self.p_man.parachute_beg)

        while self.lives != 4 and self.keep_playing:
            self.get_inputs()
            self.do_updates(word)
            self.do_outputs()

        if self.lives == 4:
            print("TERMINATED")
        else:
            print("You win!!")

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self.player_letter = self.player.guess_letter(self.player_letter)

    def do_updates(self, word):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        guess, lives = self.game_master.check_guess(self.player_letter, word)
        self.lives = lives 
        self.keep_playing = self.game_master.change_underscore(self.player_letter, word)
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """
        print(self.p_man.para_display(self.lives))

    def is_alive(self):
       pass