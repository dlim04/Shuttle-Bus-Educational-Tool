from TokenType import TokenType


def move(instruction):
    if instruction[0] == TokenType.SPECIAL_FORWARD:
        return forward(instruction[1])
    elif instruction[0] == TokenType.SPECIAL_REVERSE:
        return reverse(instruction[1])
    elif instruction[0] == TokenType.SPECIAL_LEFT:
        return left(instruction[1])
    elif instruction[0] == TokenType.SPECIAL_RIGHT:
        return right(instruction[1])


def forward(distance):
    return "The shuttle bus moved forward " + str(distance) + " space(s)"


def reverse(distance):
    return "The shuttle bus moved backward " + str(distance) + " space(s)"


def left(angle):
    return "The shuttle bus turned left " + str(angle) + " degrees"


def right(angle):
    return "The shuttle bus turned right " + str(angle) + " degrees"


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
