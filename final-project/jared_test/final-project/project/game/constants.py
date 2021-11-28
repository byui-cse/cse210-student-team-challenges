import os

#Game window constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Kerchunk!"

#Background sprite constants
BACKGROUND_SCALING = .5

#Player sprite constants
PLAYER_SCALING = .15
PLAYER_SPEED = 5

#Stone sprite constants
STONE_SCALING = .04
STONE_SPEED = 5

#Car sprite constants
CAR_SCALING = .10
CAR_SPEED = 3

#Cloud sprite constants
CLOUD_SCALING = .3
CLOUD_SPEED = -1

#Street sprite constants
STREET_SCALING = .5

def get_base():
    base = None
    bases = ["cse210-student-team-challenges/final-project/jared_test/final-project/project/game/assets", "../assets", "/assets","assets","final-project/assets"]
    for base_name in bases:
        if os.path.exists(base_name):
            base = base_name
    if base is None:
        raise Exception("Cannot find asset path. Please contact the developers.")
    return base