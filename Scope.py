class Scope:
    """
    Class to define the Scope object to be used during compilation of the whole program.
    """

    def __init__(self, line_number, instructions):
        """
        Constructor for the Scope object.
        :param line_number: The line the function is defined at
        :param instructions: The program to be compiled
        """
        self.__line_number = line_number
        self.__instructions = instructions

        self.__instructions.pop(0)
        self.__instructions.pop(len(self.__instructions) - 1)

        self.__length = len(self.__instructions)

    def get_type(self):
        """
        Getter for the type of the scope.
        :return: The type of the scope as a TokenType
        """
        return self.__type

    def get_line_number(self):
        """
        Getter for the line number the loop is declared at.
        :return: The line number the scope is declared at as an integer
        """
        return self.__line_number

    def get_instructions(self):
        """
        Getter for the list of instructions the scope performs.
        :return: The list of instructions as a 2D list
        """
        return self.__instructions

    def get_length(self):
        """
        Getter for the length of the scope.
        :return: The length of the function as an integer
        """
        return self.__length
