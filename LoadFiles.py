import io

from Settings import Settings, reset_settings


def load_instructions(filename):
    """
    Function to read a string in from a text file and return that string.
    :param filename: The name of the text file as a string
    :return: The contents of the text file as a string
    """
    try:
        file = open(filename)
    except FileNotFoundError:
        file = open(filename, "x")

    try:
        program = file.read()
        file.close()
    except io.UnsupportedOperation:
        program = ""

    return program


def load_settings():
    """
    Function to read the settings file and return a settings object that stores the settings specified in the
    Settings.txt.
    :return: The Settings object that stores the settings for the compiler
    """
    settings_file = "Settings.txt"
    try:
        file = open(settings_file)
        settings_string = file.read()
    except FileNotFoundError:
        settings_string = ""

    settings = Settings(settings_string)

    return settings


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
