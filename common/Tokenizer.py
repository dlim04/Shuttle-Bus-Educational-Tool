from common.TokenType import *


def tokenizer(program):
    """
    The tokenizer converts a program as a string into an 2D list of it's tokens, function names and integers where
    each embedded list represents a line of the program.
    :param program: The program to be run as a string
    :return: A tokenized version of the program
    """
    string = ""
    token_program = []
    current_line = []
    for character in program:
        if is_letter(character) or is_digit(character):
            string += character

        else:  # If the character isn't a letter or digit
            if string != "":  # If the current string isn't empty
                if get_keyword(string) is not None:
                    string = get_keyword(string)

                elif get_special(string) is not None:
                    string = get_special(string)

                elif get_number(string) is not None:
                    string = get_number(string)

                current_line.append(string)  # Append string to the current line
                string = ""  # Clear string

            if get_symbol(character) is not None:
                current_line.append(get_symbol(character))

            elif is_newline(character):
                token_program.append(current_line)
                current_line = []

    return token_program


def get_keyword(string):
    """
    Function that returns the keyword token of a corresponding string.
    :param string: The keyword in string form
    :return: The token of that string
    """
    keywords = {
        "function": TokenType.KEYWORD_FUNCTION,
        "for": TokenType.KEYWORD_FOR,
    }
    try:
        return keywords[string]
    except KeyError:
        return None


def get_special(string):
    """
    Function that returns the special token of a corresponding string.
    :param string: The special in string form
    :return: The token of that string
    """
    specials = {
        "forward": TokenType.SPECIAL_FORWARD,
        "reverse": TokenType.SPECIAL_REVERSE,
        "left": TokenType.SPECIAL_LEFT,
        "right": TokenType.SPECIAL_RIGHT
    }
    try:
        return specials[string]
    except KeyError:
        return None


def get_symbol(character):
    """
    Function that returns the symbol token of a corresponding character.
    :param character: The symbol in character form
    :return: The token of that character
    """
    symbols = {
        '(': TokenType.LEFT_PAREN,
        ')': TokenType.RIGHT_PAREN,
        '{': TokenType.LEFT_BRACE,
        '}': TokenType.RIGHT_BRACE,
        ';': TokenType.SEMICOLON,
    }
    try:
        return symbols[character]
    except KeyError:
        return None


def is_letter(character):
    """
    Function to determine whether a given character is a letter.
    :param character: The character to be checked
    :return: Whether the character is a letter or not as a boolean value
    """
    if ord('a') <= ord(character) <= ord('z') or ord('A') <= ord(character) <= ord('Z'):
        return True
    else:
        return False


def is_digit(character):
    """
    Function to determine whether a given character is a digit.
    :param character: The character to be checked
    :return: Whether the character is a digit or not as a boolean value
    """
    if ord('0') <= ord(character) <= ord('9'):
        return True
    else:
        return False


def get_number(string):
    """
    Function to convert a string to number if valid.
    :param string: The string to be converted
    :return: The number as an integer
    """
    num_flag = True  # Is every character in string a number
    for character in string:
        if not is_digit(character):
            num_flag = False

    if num_flag:
        return int(string)  # Then convert string to an integer
    else:
        return None


def is_whitespace(character):
    """
    Function to determine whether a given character is a whitespace character.
    :param character: The character to be checked
    :return: Whether the character is a whitespace character or not as a boolean value
    """
    if character == ' ' or character == '\n' or character == '\t' or character == '\r':
        return True
    else:
        return False


def is_newline(character):
    """
    Function to determine whether a given character is a newline character.
    :param character: The character to be checked
    :return: Whether the character is a newline character or not as a boolean value
    """
    if character == '\n':
        return True
    else:
        return False


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
