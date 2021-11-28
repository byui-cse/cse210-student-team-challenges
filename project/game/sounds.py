import arcade 
from game import K
class Sounds:
#This class uses the library resources to load the sounds
# Any file loaded that starts with :resources: will attempt to load 
# that file from the library resources instead of the project directory.

    def __init__(self):

        self.jump_sound_file = ':resources:sounds/jump2.wav'
        self.jump_sound = arcade.Sound(self.jump_sound_file)

        
        self.music_file = "project\game\sounds\music.mp3"
        self.music = arcade.Sound(self.music_file)

    def load_sound(self):
        arcade.load_sound(self.jump_sound_file)

    def play_jump_sound(self):
        self.jump_sound.play(K.JUMP_VOLUME, 0, False)
    

    def stop_sound(self):
        arcade.stop_sound()

    def play_music(self):
        self.music.play(K.MUSIC_VOLUME, 0, True)