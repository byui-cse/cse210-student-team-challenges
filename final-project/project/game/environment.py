import arcade
from game import constants

class Environment(arcade.Sprite):
    """A code template for the surface sprite. The responsibility of 
    this class of objects is to set up the surface sprite.
    """
    def __init__(self, x_value, y_value):
        """The class constructor.
        
        Args:
            self (Surface): an instance of Surface.
        """
        #Set background color
        self.background = arcade.set_background_color(arcade.csscolor.BLACK)
        
        #Set sprites and scaling
        self.surface = arcade.Sprite(":resources:images/tiles/sandCenter_rounded.png", constants.SURFACE_SCALING)
        self.star = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", constants.STAR_SCALING)

        #Set sound effect
        self.sound = arcade.Sound(":resources:sounds/hurt1.wav")

        #Initialize positions
        self.surface.center_x = x_value
        self.surface.center_y = y_value

        self.star.center_x = x_value
        self.star.center_y = y_value

    #Plays sound effect
    def play_sound(self):
        self.sound.play()