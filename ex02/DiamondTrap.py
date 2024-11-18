from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Represents a King with Baratheon and Lannister traits.
    Manages physical traits like eye and hair color.
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initializes the King with a name and alive status.
        Args:
            first_name (str): The King's first name.
            is_alive (bool): Whether the King is alive. Default is True.
        """
        super().__init__(first_name, is_alive)
        self._eyes = "brown"  # Default eye color
        self._hairs = "dark"  # Default hair color

    def get_eyes(self) -> str:
        """Returns the King's eye color."""
        return self._eyes

    def set_eyes(self, color: str) -> None:
        """
        Sets the King's eye color.
        Args:
            color (str): New color for the King's eyes.
        """
        self._eyes = color

    def get_hairs(self) -> str:
        """Returns the King's hair color."""
        return self._hairs

    def set_hairs(self, color: str) -> None:
        """
        Sets the King's hair color.
        Args:
            color (str): New color for the King's hair.
        """
        self._hairs = color

    # Define properties for eyes and hairs
    eyes = property(get_eyes, set_eyes, doc="Property for eye color.")
    hairs = property(get_hairs, set_hairs, doc="Property for hair color.")
