from TokenType import TokenType


class Function(Scope):
    """
    Class to define the Function object to be used during compilation of the whole program.
    """
    def __init__(self, line_number, instructions):
        """
        Constructor for the Function object.
        :param line_number: The line the function is defined at
        :param instructions: The program to be compiled
        """
        super().__init__(line_number, instructions)
        self.__type = TokenType.SCOPE_LOOP

        self.__name = self.__instructions[0][1]

    def get_name(self):
        """
        Getter for the name of the function.
        :return: The name of the function as a string
        """
        return self.__name
