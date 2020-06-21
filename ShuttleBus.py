from TokenType import TokenType


class ShuttleBus:
    """
    Class to define the ShuttleBus object for use when executing the program defined by the user and running the
    animation.
    """
    def __init__(self):
        """
        Constructor for the ShuttleBus class
        """
        self.__x = 0
        self.__y = 500
        self.__angle = 180

    def move(self, instruction):
        """
        Private helper method to translate the program to animation.
        :param instruction: A list with a Special token at index 0 and an integer modifier at index 1
        """
        if instruction[0] == TokenType.SPECIAL_FORWARD:
            return self.__drive(instruction[1])
        elif instruction[0] == TokenType.SPECIAL_REVERSE:
            return self.__drive(-instruction[1])
        elif instruction[0] == TokenType.SPECIAL_LEFT:
            return self.__left(instruction[1])
        elif instruction[0] == TokenType.SPECIAL_RIGHT:
            return self.__right(instruction[1])

    def __drive(self, distance):
        """
        Private helper method to animate the shuttle bus moving.
        :param distance: The amount of tiles the shuttle bus moves as an integer
        """
        double_grid_size = 64
        if self.__angle == 0:
            self.__x += distance * double_grid_size
        elif self.__angle == 90:
            self.__y += distance * double_grid_size
        elif self.__angle == 180:
            self.__x -= distance * double_grid_size
        elif self.__angle == 270:
            self.__y -= distance * double_grid_size

        # Animation goes here

        return "The shuttle bus moved forward " + str(distance) + " space(s)"

    def __left(self, angle):
        """
        Private helper method to animate the shuttle but turning left.
        :param angle: The angle the bus turns left as an integer
        """
        self.__set_angle(-angle)

        # Animation goes here

        return "The shuttle bus turned left " + str(angle) + " degrees"

    def __right(self, angle):
        """
        Private helper method to animate the shuttle but turning right.
        :param angle: The angle the bus turns right as an integer
        """
        self.__set_angle(angle)

        # Animation goes here

        return "The shuttle bus turned right " + str(angle) + " degrees"

    def __set_angle(self, angle):
        """
        Private helper method to handle which way the bus is currently facing.
        :param angle: The angle the bus has turned as an integer (positive for clockwise, negative for anti-clockwise)
        """
        self.__angle += angle
        if self.__angle > 0:
            self.__angle = self.__angle % 360
        else:
            self.__angle = -self.__angle % 360

        while self.__angle < 0:
            self.__angle += 360


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
