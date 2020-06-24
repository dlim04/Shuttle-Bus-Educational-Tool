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

    SCOPE_FUNCTION = 12
    SCOPE_LOOP = 13

    ERROR_LOGICAL_ERROR = 14


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
