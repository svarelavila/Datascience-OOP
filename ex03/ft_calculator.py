class Calculator:
    """
    A Calculator class for performing arithmetic operations between
    a vector and a object.

    Methods:
        __init__(self, vector): Init the calculator with the provided vector.

        __add__(self, object): + a object value to each element of the vec.

        __mul__(self, object): * each element of the vector by a object value.

        __sub__(self, object): - a object value from each element of the vector

        __truediv__(self, object): / each element of the vector by a object val
    """

    def __init__(self, vector):
        """
        Initializes the calculator with the provided vector.
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Returns:
            The resulting vector after addition.
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Returns:
            The resulting vector after multiplication.
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Returns:
            The resulting vector after subtraction.
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Returns:
            The resulting vector after division.

        Raises:
            ZeroDivisionError: If the object value is 0.
        """
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
