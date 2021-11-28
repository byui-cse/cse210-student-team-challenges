import os

MAX_X = 80
MAX_Y = 20
FRAME_LENGTH = 0.001
PATH = os.path.dirname(os.path.abspath(__file__))
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Kerchunk!"
BIRD_SPEED = 3
STONE_SPEED = 3
CAR_SPEED = 3
G = 2

def get_base():
    base = None
    bases = ["cse210-student-team-challenges/final-project/assets", "../assets", "/assets","assets","final-project/assets"]
    for base_name in bases:
        if os.path.exists(base_name):
            base = base_name
    if base is None:
        raise Exception("Cannot find asset path. Please contact the developers.")
    return base