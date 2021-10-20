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
        memory = 0
        self.__memory = memory
        
    @property
    def memory(self) -> float:
        return self.__memory
     
    def add(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator performs addition of memorised and provided numbers.
        If two numbers are provided: calculator performs addition between them.
        """
        if nr2 is None:
            result = self.__memory + nr
            self.__memory = result
        else:
            result = nr + nr2 
            self.__memory = result
        return result

    def subtract(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator subtracts provided number from memorised one.
        If two numbers are provided: calculator subtracts second provided number from first provided number.
        """
        if nr2 is None:
            result = self.__memory - nr
            self.__memory = result
        else:
            result = nr - nr2
            self.__memory = result
        return result

    def multiply(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator performs multiplication of memorised and provided numbers.
        If two numbers are provided: calculator performs multiplication of provided numbers.
        """
        if nr2 is None:
            result = self.__memory * nr
            self.__memory = result
        else:
            result = nr * nr2
            self.__memory = result
        return result

    def divide(self, nr: float, nr2: float = None) -> float:
        """
        If one number is provided: calculator divides memorised number by provided one.
        If two numbers are provided: calculator divides first number by second number.
        """
        if nr2 is None:
            if nr == 0:
                raise ZeroDivisionError("You can't divide by 0")
            result = self.__memory / nr
            self.__memory = result
        else:
            if nr2 == 0:
                raise ZeroDivisionError("You can't divide by 0")
            result = nr / nr2
            self.__memory = result
        return result

    def n_root(self, n: float, nr: float = None) -> float:
        """
        If one number is provided: calculator takes nth root from memorised number.
        If two numbers are provided: calculator takes nth root (first number) from provided number (second number).
        """
        if n == 0:
            raise ZeroDivisionError("The 0th root of any number is undefined")
        else:
            if nr is None:
                result = self.__memory ** (1 / float(n))
                self.__memory = result
            else:
                result = nr ** (1 / float(n))
                self.__memory = result
        return result

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
