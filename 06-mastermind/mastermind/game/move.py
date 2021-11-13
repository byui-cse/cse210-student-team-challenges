class Move: 
    """
    The guess from the player. Move is responsible for keeping track of the guess of each player. 

    sterotype: Information Holder

    atrributes: 
            _guess (List?): The numbers of the player guessed. 
    """

    def __init__(self, guess):
        """
        The class constructor. 

        Arguements: 
            self (): an instance of guess
        """
        
        self._guess = guess 

    def get_guess(self): 
        """
        Returns the guess of the player
        """

        return self._guess
