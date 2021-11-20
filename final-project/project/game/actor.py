
from game import constants
from game.point import Point
from arcade import Sprite

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position 
    and velocity in 2d space.
    Stereotype:
        Information Holder
    Attributes:
        _sprite (Sprite): The actor's sprite
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
      """The class constructor."""
      self._sprite = None
      self._position = Point(0, 0)
      self._velocity = Point(0, 0)

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position
    
    def get_sprite(self):
        """Gets the actor's sprite
        Returns:
            string: The actor's image path.
        """
        return self._sprite

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity
    
    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
        self._sprite.center_x = self._position.get_x()
        self._sprite.center_y = self._position.get_y()
    
    def set_sprite(self, text):
        """Updates the actor's image to the given value.
        
        Args:
            image (Sprite): The given value
        """
        self._sprite = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity
    
    def draw(self):
        """Draw the actor"""
        self._sprite.draw()

    def move(self):
        """Move the actor"""
        new_pos = self.get_position().add(self._velocity)
        self.set_position(new_pos)