from enum import *


class TileType(Enum):
    """
    Enumerator class to store the tiles for use in the GUI display.
    """
    STRAIGHT_ROAD = 1
    CORNER_ROAD = 2
    T_JUNCTION = 3
    CROSSROADS = 4
    DEAD_END = 5

    DIRT = 6
    GRASS = 7

    COFFEE_SHOP = 8
    LIBRARY = 9
    CHURCH = 10
    SWEET_SHOP = 11
    CANDY_SHOP = 12
    FOOTBALL_CLUB = 13
    HELIPAD = 14
    JAIL = 15
    JEWELLERY_SHOP = 16
    GAME_SHOP = 17

    BUS_STOP = 18


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
        "DEAD_END": TileType.DEAD_END,
        "DIRT": TileType.DIRT,
        "GRASS": TileType.GRASS,
        "COFFEE_SHOP": TileType.COFFEE_SHOP,
        "LIBRARY": TileType.LIBRARY,
        "CHURCH": TileType.CHURCH,
        "SWEET_SHOP": TileType.SWEET_SHOP,
        "CANDY_SHOP": TileType.CANDY_SHOP,
        "FOOTBALL_CLUB": TileType.FOOTBALL_CLUB,
        "HELIPAD": TileType.HELIPAD,
        "JAIL": TileType.JAIL,
        "JEWELLERY_SHOP": TileType.JEWELLERY_SHOP,
        "GAME_SHOP": TileType.GAME_SHOP,
        "BUS_STOP": TileType.BUS_STOP
    }
    try:
        return tiles[string]
    except KeyError:
        return TileType.DIRT


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
