import arcade 
from ZeldaGame.scaling import SCREEN_WIDTH

class Weapon(arcade.Sprite):
    
    def update(self):
        """Update the position of the sprite
    When it moves off screen to the left, remove it
    """

        # Move the sprite
        super().update()

        if (
            self.velocity[0] < 0 and self.right < 0
            or self.velocity[0] > 0 and self.left > SCREEN_WIDTH
        ):
            self.remove_from_sprite_lists()