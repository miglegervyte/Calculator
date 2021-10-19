class Calculator:

    """
        This is Calculator. It can perform basic math actions such as:
        Addition / Subtraction
        Multiplication / Division
        Take (n) root of a number
        Reset memory
        Calculator has its own memory, meaning it manipulates its starting number 0 until it is reset or two arguments
        are provided. If two arguments are provided mathematical operations are performed between them.
    """

    def __init__(self, memory: float = None) -> None:
        self.__memory = memory

    def add(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator performs addition of memorised and provided numbers.
        If two numbers are provided: calculator performs addition between them.
        """
        if nr2 is None:
            self.__memory += nr
        else:
            self.__memory = nr + nr2
        return self.__memory

    def subtract(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator subtracts provided number from memorised one.
        If two numbers are provided: calculator subtracts second provided number from first provided number.
        """
        if nr2 is None:
            self.__memory -= nr
        else:
            self.__memory = nr - nr2
        return self.__memory

    def multiply(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator performs multiplication of memorised and provided numbers.
        If two numbers are provided: calculator performs multiplication of provided numbers.
        """
        if nr2 is None:
            self.__memory *= nr
        else:
            self.__memory = nr * nr2
        return self.__memory

    def divide(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator divides memorised number by provided one.
        If two numbers are provided: calculator divides first number by second number.
        """
        if nr2 is None:
            if nr == 0:
                raise ZeroDivisionError("You can't divide by 0")
            self.__memory /= nr
        else:
            if nr2 == 0:
                raise ZeroDivisionError("You can't divide by 0")
            self.__memory = nr / nr2
        return self.__memory

    def n_root(self, n: float, nr: float = None) -> float:
        """
        If one number is provided: calculator takes nth root from memorised number.
        If two numbers are provided: calculator takes nth root (first number) from provided number (second number).
        """
        if n == 0:
            raise ZeroDivisionError("The 0th root of any number is undefined")
        else:
            if nr is None:
                self.__memory = self.__memory ** (1 / float(n))
            else:
                self.__memory = nr ** (1 / float(n))
        return self.__memory

    def check_memory(self) -> float:
        """
        Checks memorised number.
        """
        return self.__memory

    def reset_memory(self) -> float:
        """
        Resets memorised number to 0.
        """
        self.__memory = 0
        return self.__memory
