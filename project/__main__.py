from game.director import Screen
from game.start_screen import QuitButton, StartScreen
from game import K

import arcade
import os



def main():
    # file_path = os.path.dirname(os.path.abspath(__file__))
    # os.chdir(file_path)

    start = starting_screen()
    if start == True:
        start_game()

def start_game():
    screen = Screen(K.SCREEN_WIDTH, K.SCREEN_HEIGHT, K.SCREEN_TITLE)
    screen.draw_background() # Must be called first
    screen.setup()
    screen.create_player()
    arcade.run() #Turn on the infinite loop to keep the screen opened

def starting_screen():
    START_SCREEN_TITLE = "Welcome to Crazy Lab Game"
    window = StartScreen(K.SCREEN_WIDTH, K.SCREEN_HEIGHT, START_SCREEN_TITLE)
    window.set_background()

    arcade.run()
    if window.start == True:
        return True
    
if __name__ == "__main__":
    main()