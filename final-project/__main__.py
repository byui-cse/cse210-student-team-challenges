import arcade
from ZeldaGame.zelda import *

def start():
    app = ZeldaGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()

if __name__ == "__main__":
    start()