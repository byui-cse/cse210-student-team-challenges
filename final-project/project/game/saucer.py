import arcade
from game import constants

class Saucer(arcade.Sprite):
    """A code template for the saucer sprite. The responsibility of 
    this class of objects is to set up the saucer sprite.
    """
    def __init__(self, x_value, y_value, angle, x_speed):
        """The class constructor.
        
        Args:
            self (Saucer): an instance of saucer.
        """
        #Set sprites and scaling
        self.sprite = arcade.Sprite(":resources:images/tiles/switchGreen.png", constants.SAUCER_SCALING)

        #Set sound effect
        self.sound = arcade.Sound(":resources:sounds/explosion2.wav")

        #Initialize Position, direction, speed
        self.sprite.center_x = x_value
        self.sprite.center_y = y_value
        self.sprite.angle = angle
        self.sprite.change_x = x_speed

    #Plays sound effect
    def play_sound(self):
        self.sound.play()

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH