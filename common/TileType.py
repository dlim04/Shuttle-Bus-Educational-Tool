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


def string_to_tile_type(string):
    """
    Function to find the matching TileType to a given string.
    :param string: The name of the TileType
    :return: The TileType
    """
    tiles = {
        "STRAIGHT_ROAD": TileType.STRAIGHT_ROAD,
        "CORNER_ROAD": TileType.CORNER_ROAD,
        "T_JUNCTION": TileType.T_JUNCTION,
        "CROSSROADS": TileType.CROSSROADS,
        "DIRT": TileType.DIRT,
        "GRASS": TileType.GRASS,
        "COFFEE_SHOP": TileType.COFFEE_SHOP,
        "LIBRARY": TileType.LIBRARY,
        "CHURCH": TileType.CHURCH,
        "SWEET_SHOP": TileType.SWEET_SHOP,
        "CANDY_SHOP": TileType.CANDY_SHOP,
        "FOOTBALL_CLUB": TileType.FOOTBALL_CLUB
    }
    try:
        return tiles[string]
    except KeyError:
        return TileType.DIRT


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
