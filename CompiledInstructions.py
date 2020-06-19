class CompiledInstructions:
    """
    Class to define the CompiledInstructions object to be run by the shuttlebus.
    """
    def __init__(self, lexically_correct, compiled_correct, error_message, instructions):
        """
        Constructor for the CompiledInstructions object.
        :param lexically_correct: Whether the instructions written by the user are lexically correct as a boolean
        :param compiled_correct: Whether the instructions written by the user were compiled correctly as a boolean
        :param error_message: The error message from the lexical analysis (None if lexically correct) as a string
        :param instructions: The compiled instructions as a 2D list
        """
        self.__lexically_correct = lexically_correct
        self.__compiled_correct = compiled_correct
        self.__error_message = error_message
        self.__instructions = instructions

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

    def get_instructions(self):
        """
        Getter for the compiled instructions.
        :return: The compiled instructions as a 2D array
        """
        return self.__instructions
