import arcade 
class Sounds:
    def __init__(self):
        self.jump_sound_file = ':resources:sounds/jump2.wav'
        self.sound = arcade.Sound(self.jump_sound_file)
    def load_sound(self):
        arcade.load_sound(self.jump_sound_file)

    def play_sound(self):
        self.sound.play(1, 0, False)

    def stop_sound(self):
        arcade.stop_sound()
