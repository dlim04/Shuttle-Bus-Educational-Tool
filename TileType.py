from enum import *


class TileType(Enum):
    """
    Enumerator class to store the tiles for use in the GUI display.
    """
    STRAIGHT_ROAD = 1
    CORNER_ROAD = 2
    T_JUNCTION = 3
    CROSSROADS = 4

    DIRT = 5
    GRASS = 6

    COFFEE_SHOP = 7
    LIBRARY = 8
    CHURCH = 9
    SWEET_SHOP = 10
    CANDY_SHOP = 11
    FOOTBALL_CLUB = 12


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
