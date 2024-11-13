class Calculator:
    """"Do calculations between two vectors"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the dot product of two vectors and print the result.

        Parameters:
        V1 (list of float): The first vector.
        V2 (list of float): The second vector.
        """
        dot_product = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {dot_product:.1f}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate vector subtraction and print result

        Parameters:
        V1 (list of float): The first vector.
        V2 (list of float): The second vector.
        """
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate vector addtion and print result

        Parameters:
        V1 (list of float): The first vector.
        V2 (list of float): The second vector.
        """
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")

