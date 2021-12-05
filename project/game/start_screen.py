import arcade
from arcade.color import BLACK
import arcade.gui
import os
import time
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Welcome to Crazy Lab Game"

# Method for handling click events
# Create a child class
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class StartScreen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # # Set the working directory (where we expect to find files) to the same
        # # directory this .py file is in


        # Background image will be stored in this variable
        self.background = None

        self.start = False
        # Set background color
        arcade.set_background_color(arcade.color.BLACK)

        # a UIManager to handle the UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, background='#000')
        self.v_box.add(start_button.with_space_around(bottom=20))

        # Again, method 1. Use a child class to handle events.
        quit_button = QuitButton(text="Quit", width=200)
        self.v_box.add(quit_button)

        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        start_button.on_click = self.on_click_start

        
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def set_background(self):
        # Load the background image. Do this in the setup so we don't keep reloading it all the time.
        self.background = arcade.load_texture("project/game/images/lab_background.png")

    def on_click_start(self, event):
        self.start = True
        arcade.exit()

    # def close(self):
    #     """ Close the Window. """
    #     super().close()
    #     pyglet.clock.unschedule(self._dispatch_updates)

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,self.background)

        self.manager.draw()


# window = StartScreen(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# window.set_background()
# arcade.run()