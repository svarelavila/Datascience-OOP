from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """The mad King himself"""
    
    def __init__(self, first_name, is_alive=True):
        """Initializes the king, a cross between a Baratheon and Lannister"""
        super().__init__(first_name, is_alive)
        self._eyes = "brown"  # Valor predeterminado para los ojos
        self._hairs = "dark"  # Valor predeterminado para el cabello

    def get_eyes(self) -> str:
        """Getter for eye color"""
        return self._eyes

    def set_eyes(self, color: str) -> None:
        """Setter for eye color"""
        self._eyes = color

    def get_hairs(self) -> str:
        """Getter for hair color"""
        return self._hairs

    def set_hairs(self, color: str) -> None:
        """Setter for hair color"""
        self._hairs = color

    # Definición de propiedades con documentación corregida
    eyes = property(get_eyes, set_eyes, doc="Property for eye color")
    hairs = property(get_hairs, set_hairs, doc="Property for hair color")
