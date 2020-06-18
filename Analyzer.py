from TokenType import *


def analyzer(program):
    """
    Function to perform lexical analysis on the tokenized version of the program.
    :param program: The tokenized version of the program
    :return: An error message as a string
    """
    left_paren = []
    right_paren = []
    left_brace = []
    right_brace = []

    line_counter = 0
    for line in program:
        line_counter += 1

        if len(line) > 0:
            last_object = line[len(line) - 1]
            if last_object != TokenType.SEMICOLON and last_object != TokenType.LEFT_BRACE and last_object != TokenType.RIGHT_BRACE:
                return "May be missing a semicolon or brace in line " + str(line_counter)

        for each in line:
            if each == TokenType.LEFT_PAREN:
                left_paren.append(line_counter)

            elif each == TokenType.RIGHT_PAREN:
                right_paren.append(line_counter)

            elif each == TokenType.LEFT_BRACE:
                left_brace.append(line_counter)

            elif each == TokenType.RIGHT_BRACE:
                right_brace.append(line_counter)

    if len(left_brace) > len(right_brace):
        return "Brace missing closing brace"
    elif len(right_brace) > len(left_brace):
        return "Brace missing opening brace"

    line_missing = line_number_match(left_paren, right_paren)
    if line_missing is not None:
        return "Parameter should only be on one line (parenthesis may be missing) in line " + str(line_missing)


def line_number_match(array1, array2):
    """
    Function that compares two lists of line numbers and determines which line numbers are missing from either array.
    :param array1: A list to be compared
    :param array2: A list to be compared
    :return: Where in the program there is a parenthesis missing as an integer
    """
    if len(array1) < len(array2):
        for number in array1:
            try:
                array2.remove(number)
            except ValueError:
                return number
        return array2[0]

    else:
        for number in array2:
            try:
                array1.remove(number)
            except ValueError:
                return number
        if len(array1) != 0:
            return array1[0]
        else:
            return None
