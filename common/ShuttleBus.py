from common.TokenType import TokenType


class ShuttleBus:
    """
    Class to define the ShuttleBus object for use when executing the program defined by the user and running the
    animation.
    """

    def __init__(self):
        """
        Constructor for the ShuttleBus class
        """
        self.__x = 2
        self.__y = 0
        self.__angle = 180

    def drive(self, distance):
        """
        Helper method to animate the shuttle bus moving.
        :param distance: The amount of tiles the shuttle bus moves as an integer
        """
        if self.__angle == 0:
            self.__y -= distance
        elif self.__angle == 90:
            self.__x -= distance
        elif self.__angle == 180:
            self.__y += distance
        elif self.__angle == 270:
            self.__x += distance

    def left(self, angle):
        """
        Helper method to animate the shuttle bus turning left.
        :param angle: The angle the bus turns left as an integer
        """
        self.__set_angle(angle)

    def right(self, angle):
        """
        Helper method to animate the shuttle bus turning right.
        :param angle: The angle the bus turns right as an integer
        """
        self.__set_angle(-angle)

    def __set_angle(self, angle):
        """
        Private helper method to handle which way the bus is currently facing.
        :param angle: The angle the bus has turned as an integer (positive for clockwise, negative for anti-clockwise)
        """
        self.__angle += angle
        if self.__angle > 0:
            self.__angle = self.__angle % 360

        while self.__angle < 0:
            self.__angle += 360

    def get_x(self):
        """
        Getter for the x ordinate of the shuttle bus.
        :return: The x ordinate of the function as an integer
        """
        return self.__x

    def get_y(self):
        """
        Getter for the y ordinate of the shuttle bus.
        :return: The y ordinate of the function as an integer
        """
        return self.__y

    def get_angle(self):
        """
        Getter for the angle of the shuttle bus.
        :return: The angle of the function as an integer
        """
        return self.__angle


def move(instruction):
    """
    Function to display text describing what instruction the shuttle bus has carried out
    :param instruction: A list with a Special token at index 0 and an integer modifier at index 1
    """
    if instruction[0] == TokenType.SPECIAL_FORWARD:
        return "The shuttle bus moved forward " + str(instruction[1]) + " space(s)"
    elif instruction[0] == TokenType.SPECIAL_REVERSE:
        return "The shuttle bus reversed " + str(instruction[1]) + " space(s)"
    elif instruction[0] == TokenType.SPECIAL_LEFT:
        return "The shuttle bus turned left " + str(instruction[1]) + " degrees"
    elif instruction[0] == TokenType.SPECIAL_RIGHT:
        return "The shuttle bus turned right " + str(instruction[1]) + " degrees"


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
