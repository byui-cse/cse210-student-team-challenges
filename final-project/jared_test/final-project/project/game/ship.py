import arcade
from game import constants

class Ship(arcade.Sprite):
    """A code template for the ship sprite. The responsibility of 
    this class of objects is to setup the ship sprite.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Ship): an instance of Ship.
        """
        #Set sprite and scale
        self.sprite = arcade.Sprite(":resources:images/space_shooter/playerShip2_orange.png", constants.SHIP_SCALING)
        self.bomb = arcade.Sprite(":resources:images/topdown_tanks/tankRed_barrel1_outline.png", constants.BOMB_SCALING)

        #Set sound effect
        self.sound = arcade.Sound(":resources:sounds/lose4.wav")

        #Position, angle, direction, speed
        self.sprite.center_x = 64
        self.sprite.center_y = 490
        self.sprite.angle = 270
        self.sprite.change_x = constants.SHIP_SPEED

    #Wraps around edge of screen
    def wraps_screen(self):
        if self.sprite.left > constants.SCREEN_WIDTH:
            self.sprite.right = 0
        elif self.sprite.right < 0:
            self.sprite.left = constants.SCREEN_WIDTH

    #Movement and actions
    def move_right(self):
        self.sprite.change_x = constants.SHIP_SPEED
        self.sprite.angle = 270

    def move_left(self):
        self.sprite.change_x = -constants.SHIP_SPEED
        self.sprite.angle = 90

    def drop_bomb(self):
        self.bomb.center_x = self.sprite.center_x
        self.bomb.center_y = self.sprite.center_y
        self.sound.play()
        self.bomb.change_y = constants.BOMB_SPEED