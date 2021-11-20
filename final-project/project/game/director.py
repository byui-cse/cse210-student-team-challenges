from time import sleep
from game import constants
from game import bird
from game import point
from game import stone
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
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self.start_game()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        #self.background = None
        self.background = arcade.load_texture("cse210-student-team-challenges/final-project/assets/background.png")
        #arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        self._bird = bird.Bird()
        self._keep_playing = True
        self._direction = 1
        self._drop_stone = False
        self._stone_list = []
        arcade.run()

    def on_draw(self):
        """Action for every time the game draws. This is the main loop of the game.
        
        Args:
            self (Director): an instance of Director.
        """
        self._get_inputs()
        self._do_updates()
        self._do_outputs()

    def on_key_press(self, key, modifiers):
        """Action for keypresses.
        
        Args:
            self (Director): an instance of Director.
        """
        if key == arcade.key.D:
            self._direction = 1
        elif key == arcade.key.A:
            self._direction = -1
        elif key == arcade.key.SPACE:
            self._drop_stone = True

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
        # Check if we are changing direction
        if self._direction == 1:
            self._bird.move_right()
        elif self._direction == -1:
            self._bird.move_left()
        # Check if dropping stone, and if so drop it, and reset the flag
        if self._drop_stone:
            self._stone_list.append(stone.Stone(self._bird.get_position()))
            self._drop_stone = False

    def _do_outputs(self):
        """Outputs the important game information for each round of play. 

        Args:
            self (Director): An instance of Director.
        """
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)
        self._bird.move()
        self._bird.draw()
        for stone in self._stone_list:
            stone.move()
            stone.draw()
        arcade.finish_render()