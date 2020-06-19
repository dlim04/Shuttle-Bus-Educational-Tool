from enum import *


class TokenType(Enum):
    """
    Enumerator class to store the tokens for program syntax.
    """
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    SEMICOLON = 5

    KEYWORD_FUNCTION = 6
    KEYWORD_FOR = 7
    
    SPECIAL_FORWARD = 8
    SPECIAL_REVERSE = 9
    SPECIAL_LEFT = 10
    SPECIAL_RIGHT = 11


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    print('Press any enter to close window . . . ')
