import io

from Settings import Settings


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
    except FileNotFoundError:
        reset_settings()
        file = open(settings_file)

    settings_string = file.read()
    settings = Settings(settings_string)

    if not settings.is_settings_complete():
        reset_settings()
        settings_string = file.read()
        settings = Settings(settings_string)

    return settings


def reset_settings():
    """
    Procedure to reset the Settings.txt file to it's standard settings.
    """
    file = open("Settings.txt", "w")
    file.write("instructions_filename = Instructions.txt\n"
               "logical_loop_limit = 1000")
    file.close()


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run run.py')
    input('Press any enter to close window . . . ')
