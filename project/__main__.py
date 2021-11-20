# def main(screen):
#     pass
from game.director import Screen
from game import constants
import arcade

def main():
    screen = Screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    screen.create_player()
    arcade.run() #Turn on the infinite loop to keep the screen opened


if __name__ == "__main__":
    main()