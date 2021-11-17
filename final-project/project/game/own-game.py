import arcade

#Constants
SPRITE_SCALING = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Own-game.py"

MOVEMENT_SPEED = 5


class Screen(arcade.Window):
    #The inheritance of the window class automatically starts the screen
    #Is important to notice that the method arcade.open_window is in the arcade.Window class
    #Also is important to notice that the Window class creates the window in the __init__
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        #Creating an instance that manages the players
        self.sprite_list = arcade.SpriteList()
        #Setting Background color
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def on_draw(self):
        """
        Render the screen, and show the sprites with the .draw() method
        """

        # This command has to happen before we start drawing
        arcade.start_render()
        self.sprite_list.draw()

        # Draw all the sprites.
    def create_player(self):
        """Create the player sprite, specify his position and append it to the list of all sprites"""
        self.player = arcade.Sprite("player.png", SPRITE_SCALING)
        self.player.center_y = self.height / 2  #Sets the y and x position of the sprite
        self.player.left = 10
        self.sprite_list.append(self.player)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


    def on_update(self, delta_time):
        """ Update the movement data done in the key detecting functions"""

        # Move the player
        self.sprite_list.update()

def main():
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    screen.create_player()
    arcade.run() #Turn on the infinite loop to keep the screen opened


main()