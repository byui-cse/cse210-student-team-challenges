from game.roster import Roster
from game.guess import Guess
from game.board import Board

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._board = None
        self._keep_playing = True
        self._roster = Roster()
        self._guess1 = Guess()
        self._guess2 = Guess()
        self._randomnum = Guess.get_random_number(self)
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        self._roster.add_players()
        print()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        #player names
        p1 = self._roster.players[0]
        p2 = self._roster.players[1]
        #player guesses
        g1 = self._guess1.user_guess
        g2 = self._guess2.user_guess
        #answer keys
        h1 = self._guess1.answer_key
        h2 = self._guess2.answer_key

        self._board = Board(p1, p2, g1, g2, h1, h2)
        # display the game board
        self._board.print()
        # get next player's move
        currentp = self._roster.get_current()
        print(f"{currentp}'s turn:")
        #I made guess a self variable so that we could use it throughout the director class.
        if currentp == p1:
            self._guess1.get_user_guess()
        else:
            self._guess2.get_user_guess()
        print()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        self._guess1.set_user_key(self._randomnum)
        self._guess2.set_user_key(self._randomnum)
        
 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the user has guessed the number in the
        right sequence.

        Args:
            self (Director): An instance of Director.
        """
        #Changed this to is_done for our solution
        stop1 = self._guess1.keep_playing()
        stop2 = self._guess2.keep_playing()
        if stop1 or stop2:
            winner = self._roster.get_current()
            print(f"{winner} won!")
            self._keep_playing = False
        self._roster.next_player()