import arcade 
class Sounds:
    # def load_sound():
    #     arcade.load_sound('project\game\sounds\quick-jump.wav')

    def play_sound():
        arcade.load_sound('project\game\sounds\quick-jump.wav')
        arcade.play_sound(1, 0, False)  

    def stop_sound():
        arcade.stop_sound()
