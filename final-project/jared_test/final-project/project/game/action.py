class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    This class doesn't do anything on its own, but other classes extend it and do things.
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        raise NotImplementedError("execute not implemented in superclass")