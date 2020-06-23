class Settings:
    """
    Class to define the Settings object for use when configuring the compiler.
    """
    def __init__(self, instructions_filename, logical_loop_limit, settings_complete):
        """
        Constructor for the Settings object.
        :param instructions_filename: The name of the file the instructions for the compiler is stored at as a string
        :param logical_loop_limit: The logical loop limit as an integer
        :param settings_complete: Whether all the setting values are satisfied as a boolean value
        """
        self.__instructions_filename = instructions_filename
        self.__logical_loop_limit = logical_loop_limit
        self.__settings_complete = settings_complete

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

    def is_settings_complete(self):
        """
        Getter for whether all the settings values are satisfied.
        :return: Whether all the settings values are as a boolean
        """
        return self.__settings_complete


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
