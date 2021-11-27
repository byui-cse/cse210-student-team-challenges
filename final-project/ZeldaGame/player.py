import arcade

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        #images
        #front run image
        texture = arcade.load_texture("cse210-student-team-challenges/final-project/images/front_run1.png")
        self.textures.append(texture)
        #back run changes
        texture = arcade.load_texture("cse210-student-team-challenges/final-project/images/back_run1.png")
        self.textures.append(texture)
        #right run image
        texture = arcade.load_texture("cse210-student-team-challenges/final-project/images/right_run1.png")
        self.textures.append(texture)
        #left run image
        texture = arcade.load_texture("cse210-student-team-challenges/final-project/images/left_run1.png")
        self.textures.append(texture)

        #By default, face front
        self.texture = self.textures[0]
        

        # the top line is equivalent to:
        #self.set_texture(0)

    def update(self):
        super().update()
        #figure out if we should face all 4 position
        if self.change_x > 0:
            self.set_texture(2)
        elif self.change_x < 0:
            self.set_texture(3)
        if self.change_y > 0:
            self.set_texture(1)
        elif self.change_y < 0:
            self.set_texture(0)