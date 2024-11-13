from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Baratheon character with the
        provided first name.

        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool): The alive status of the character.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Mark the character as not alive."""
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of
        the Baratheon character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a formal string representation of
        the Baratheon character.
        """
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a Lannister character with the provided first name.

        Parameters:
            first_name (str): The first name of the character.
            is_alive (bool): The alive status of the character.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """Mark the character as not alive."""
        self.is_alive = False

    def __str__(self):
        """
        Return a string representation of
        the Lannister character.
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """
        Return a formal string representation of
        the Lannister character.
        """
        return self.__str__()


    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """
        Create a Lannister character instance with custom is_alive status.
        Returns:
            Lannister: An instance of the Lannister character.
        """
        return cls(first_name, is_alive)
