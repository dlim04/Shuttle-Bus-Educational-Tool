def load_instructions(filename):
    """
    Function to read a string in from a text file and return that string.
    :param filename: The name of the text file as a string
    :return: The contents of the text file as a string
    """
    file = open(filename)
    program = file.read()
    file.close()
    return program


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
