class Settings:
    """
    Class to define the Settings object for use when configuring the compiler.
    """
    def __init__(self, settings_string):
        """
        Constructor for the Settings object.
        :param settings_string: A string containing the desired settings
        """
        self.__instructions_filename = "Instructions.txt"
        self.__logical_loop_limit = 1000

    def get_instructions_filename(self):
        """
        Getter for the filename the instructions for the compiler is stored at.
        :return: The filename of the instructions as a string
        """
        return self.__instructions_filename

    def get_logical_loop_limit(self):
        """
        Getter for the logical loop limit.
        :return: The logical loop limit as an integer
        """
        return self.__logical_loop_limit


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')