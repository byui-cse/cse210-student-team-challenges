from game.player import Player
from game.background import Background
from game.platforms import Platforms
from game import constants

import arcade
import time

class Screen(arcade.Window):
    #The inheritance of the window class automatically starts the screen
    #Is important to notice that the method arcade.open_window is in the arcade.Window class
    #Also is important to notice that the Window class creates the window in the __init__
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        #Creating an instance that manages the players
        self.sprite_list = arcade.SpriteList()
        #Setting Background color
        arcade.set_background_color(arcade.color.BLACK)

        self.platforms = Platforms.make_platforms(constants.SCREEN_WIDTH * 5, 0, (106, 106, 86), 0.7, 0.5)

    def on_draw(self):
        """
        Render the screen, and show the sprites with the .draw() method
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        self.sprite_list.draw()

        # Draw all the sprites.
        self.platforms.draw()


    def create_player(self):
        
        """Create the player sprite, specify his position and append it to the list of all sprites"""
        self.player = Player("project/game/images/player.png", constants.SPRITE_SCALING) #THE PLAYER OBJECT
        self.player.center_y = self.height / 2  #Sets the y and x position of the sprite
        self.player.left = 10
        self.sprite_list.append(self.player)

        # self.physics_engine = arcade.PhysicsEnginePlatformer(
        #     self.player, gravity_constant=constants.GRAVITY, walls= self.sprite_list)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player.change_y = constants.PLAYER_JUMP_SPEED
        
        elif key == arcade.key.DOWN:
            self.player.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        # if key == arcade.key.UP or key == arcade.key.DOWN:
        #     self.player.change_y = 0
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def draw_background(self):
        self.background = Background("project/game/images/lab_background.png", constants.BACKGROUND_SCALE)
        self.background.center_y = 280 #Sets the y and x position of the sprite
        self.background.left = 0
        self.sprite_list.append(self.background)

    def on_update(self, delta_time):
        """ Update the movement data done in the key detecting functions"""

        # Move the player
        self.sprite_list.update()

        # Allow the platforms to keeep moving           
        self.platforms.center_x -= 1   
    
    def gravity(self):
        # This should be it's own class, and get called from the init.
        pass

