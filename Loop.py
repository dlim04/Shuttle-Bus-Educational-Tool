from Scope import Scope
from TokenType import TokenType


class Loop(Scope):
    """
    Class to define the Loop object to be used during compilation of the whole program.
    """
    def __init__(self, line_number, instructions):
        """
        Constructor for the Loop object.
        :param line_number: The line the loop is defined at
        :param instructions: The program to be compiled
        """
        super().__init__(line_number, instructions)
        self.__loop_count = instructions[0][2]
        self._instructions.pop(0)
        self._instructions.pop(len(self._instructions) - 1)
        self._type = TokenType.SCOPE_LOOP

    def expand(self):
        """
        Method to expand the contents of the loop.
        :return: The expanded contents of the loop as a 2D array
        """
        expanded_instructions = []

        for i in range(0, self.__loop_count):
            expanded_instructions += self._instructions

        return expanded_instructions


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
