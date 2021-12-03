import arcade
from game import constants

class Meteor(arcade.Sprite):
    """A code template for the meteor sprite. The responsibility of 
    this class of objects is to setup the meteor sprite.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Meteor): an instance of Meteor.
        """
        #Set sprite and scale
        self.sprite = arcade.Sprite(":resources:images/space_shooter/meteorGrey_big3.png", constants.METEOR_SCALING)

        #Position, direction, speed
        self.sprite.center_x = 350
        self.sprite.center_y = 350
        self.sprite.change_x = constants.METEOR_SPEED

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH