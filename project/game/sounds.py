import arcade 
from game import K
class Sounds:
    def __init__(self):
        self.sound_file = 'project/game/sounds/quick-jump.wav'
        self.sound = arcade.Sound(self.sound_file)
        
        self.music_file = "project\game\sounds\music.mp3"
        self.music = arcade.Sound(self.music_file)

    def load_sound(self):
        arcade.load_sound(self.sound_file)

    def play_sound(self):
        self.sound.play(1, 0, False)

    def stop_sound(self):
        arcade.stop_sound()

    def play_music(self):
        self.music.play(K.MUSIC_VOLUME, 0, True)