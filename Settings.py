from re import split


class Settings:
    """
    Class to define the Settings object for use when configuring the compiler.
    """
    def __init__(self, settings_string):
        """
        Constructor for the Settings object.
        :param settings_string: A string containing the desired settings
        """
        settings_list = split('\n', settings_string)
        for i in range(0, len(settings_list)):
            settings_list[i] = split('=', settings_list[i])
            for identifier in settings_list[i]:
                identifier.replace(' ', '')

        instructions_filename = settings_list[0][1]
        instructions_filename_is_valid = instructions_filename[-4:] == ".txt"

        logical_loop_limit = settings_list[1][1]

        try:
            logical_loop_limit = int(logical_loop_limit)
            logical_loop_limit_is_valid = logical_loop_limit > 0
        except ValueError:
            logical_loop_limit_is_valid = False

        if instructions_filename_is_valid and logical_loop_limit_is_valid:
            self.__instructions_filename = instructions_filename
            self.__logical_loop_limit = logical_loop_limit
            self.__settings_complete = True

        else:
            reset_settings()
            self.__instructions_filename = "Instructions.txt"
            self.__logical_loop_limit = 1000
            self.__settings_complete = True

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


def reset_settings():
    """
    Procedure to reset the Settings.txt file to it's standard settings.
    """
    file = open("Settings.txt", "w")
    file.write("instructions_filename = Instructions.txt\n"
               "logical_loop_limit = 1000")
    file.close()