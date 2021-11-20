from time import sleep
from game import constants
from game import bird
from game import point
import arcade 

class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._keep_playing = True
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self.start_game()

        #self._input_service = input_service
        #self._output_service = output_service
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        self._bird = bird.Bird()
        arcade.run()

    def on_draw(self):
        """Action for every time the game draws. This is the main loop of the game.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_inputs()
        self._do_updates()
        self._do_outputs()

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        pass
    def _do_updates(self):
        """Updates the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        self._bird.set_velocity(point.Point(1,1))
        self._bird.move()
        pass
    def _do_outputs(self):
        """Outputs the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        arcade.start_render()
        self._bird._sprite._speed = 400
        self._bird.draw()
        arcade.finish_render()
        pass