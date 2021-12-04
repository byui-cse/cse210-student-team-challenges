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
        self.reward_sound = arcade.Sound(":resources:sounds/upgrade2.wav")
        self.new_level_sound = arcade.Sound(":resources:sounds/upgrade5.wav")

        self.music_file = "project\game\sounds\music.mp3"
        self.music = arcade.Sound(self.music_file)

        self.music2_file = "project/game/sounds/final_boss.mp3"
        self.music2 = arcade.Sound(self.music2_file)
    
    def load_sound(self, sound_file):
        arcade.load_sound(sound_file)
    
    def play_jump_sound(self):
        self.jump_sound.play(K.JUMP_VOLUME, 0, False)

    def play_collision_sound(self):
        self.collision_sound.play(K.JUMP_VOLUME, 0, False)
        
        
    

    def stop_sound(self,stop):
        self.music.stop(stop)
        
    
    def play_reward_sound(self):
        self.reward_sound.play(K.REWARD_VOLUME, 0, False)

    def play_newlevel_sound(self):
        self.new_level_sound.play(K.NEW_LEVEL_VOLUME, 0, False)

    def play_music(self):
        return self.music.play(K.MUSIC_VOLUME, 0, True)

    def play_nlevel_music(self):
        return self.music2.play(K.NEW_LEVEL_MUSIC_VOLUME, 0, True)