import arcade 
class Sounds:
    def __init__(self):
        self.sound_file = 'project\game\sounds\quick-jump.wav'
        self.sound = arcade.Sound(self.sound_file)
    def load_sound(self):
        arcade.load_sound(self.sound_file)

    def play_sound(self):
        self.sound.play(1, 0, False)
        arcade.play_sound(1, 0, False)  

    def stop_sound(self):
        arcade.stop_sound()
