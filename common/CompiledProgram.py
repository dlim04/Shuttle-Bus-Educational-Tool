class CompiledProgram:
    """
    Class to define the CompiledProgram object to be run by the shuttle bus.
    """
    def __init__(self, lexically_correct, compiled_correct, error_message, instructions_line_count, code):
        """
        Constructor for the CompiledProgram object.
        :param instructions_line_count:
        :param lexically_correct: Whether the instructions written by the user are lexically correct as a boolean
        :param compiled_correct: Whether the instructions written by the user were compiled correctly as a boolean
        :param error_message: The error message from the lexical analysis (None if lexically correct) as a string
        :param code: The compiled instructions as a 2D list
        """
        self.__lexically_correct = lexically_correct
        self.__compiled_correct = compiled_correct
        self.__error_message = error_message
        self.__instructions_line_count = instructions_line_count
        self.__code = code

    def is_lexically_correct(self):
        """
        Getter for whether the instructions are lexically correct.
        :return: Whether the instructions are lexically correct as a boolean
        """
        return self.__lexically_correct

    def is_compiled_correct(self):
        """
        Getter for whether the instructions have compiled correctly.
        :return: Whether the instructions have compiled correctly as a boolean
        """
        return self.__compiled_correct

    def get_error_message(self):
        """
        Getter for the error message generated from lexical analysis.
        :return: The error message as a string
        """
        return self.__error_message

    def get_code(self):
        """
        Getter for the compiled instructions.
        :return: The compiled instructions as a 2D array
        """
        return self.__code

    def get_instructions_line_count(self):
        """
        Getter for the number of lines written in the instructions.
        :return: The number of lines written in the instructions as an integer
        """
        return self.__instructions_line_count


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
