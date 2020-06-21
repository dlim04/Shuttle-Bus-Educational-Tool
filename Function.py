from Scope import Scope
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

        self.__name = self._instructions[0][1]
        self._instructions.pop(0)
        self._instructions.pop(len(self._instructions) - 1)
        self._type = TokenType.SCOPE_FUNCTION

    def get_name(self):
        """
        Getter for the name of the function.
        :return: The name of the function as a string
        """
        return self.__name


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
