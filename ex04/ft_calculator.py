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
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate vector subtraction and print result

        Parameters:
        V1 (list of float): The first vector.
        V2 (list of float): The second vector.
        """
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate vector addtion and print result

        Parameters:
        V1 (list of float): The first vector.
        V2 (list of float): The second vector.
        """
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
