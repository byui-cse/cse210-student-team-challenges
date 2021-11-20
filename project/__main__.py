# def main(screen):
#     pass
from game.director import Screen
from game import K
import arcade

def main():
    screen = Screen(K.SCREEN_WIDTH, K.SCREEN_HEIGHT, K.SCREEN_TITLE)
    screen.draw_background() # Must be called first
    screen.setup()
    screen.create_player()
    arcade.run() #Turn on the infinite loop to keep the screen opened


if __name__ == "__main__":
    main()