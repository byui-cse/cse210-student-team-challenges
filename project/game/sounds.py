import arcade 
from game import K
class Sounds:
#This class uses the library resources to load the sounds
# Any file loaded that starts with :resources: will attempt to load 
# that file from the library resources instead of the project directory.

    def __init__(self):

       # self.jump_sound_file = ':resources:sounds/jump2.wav'
        self.jump_sound = arcade.Sound(':resources:sounds/jump2.wav')
        self.collision_sound = arcade.Sound(':resources:sounds/hit3.wav')

        
        self.music_file = "project\game\sounds\music.mp3"
        self.music = arcade.Sound(self.music_file)

    
    def load_sound(self, sound_file):
        arcade.load_sound(sound_file)
    
    def play_jump_sound(self):
        self.jump_sound.play(K.JUMP_VOLUME, 0, False)

    def play_collision_sound(self):
        self.collision_sound.play(K.JUMP_VOLUME, 0, False)
        
    
        
    

    def stop_sound(self):
        arcade.stop_sound()

    def play_music(self):
        self.music.play(K.MUSIC_VOLUME, 0, True)