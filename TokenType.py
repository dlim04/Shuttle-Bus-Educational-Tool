from enum import *


class TokenType(Enum):
    """
    Enumerator class to store the tokens for program syntax.
    """
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    LEFT_BRACKET = 5
    RIGHT_BRACKET = 6
    SEMICOLON = 7

    KEYWORD_FUNCTION = 8
    KEYWORD_FOR = 9
