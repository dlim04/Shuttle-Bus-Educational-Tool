from common.TileType import TileType, string_to_tile_type
from pygame import image


class Tile:
    """
    Class to define the Tile object for use when drawing the map in the GUI.
    """

    def __init__(self, tile_type, angle):
        """
        Constructor for the Tile class
        """
        self.__is_road = determine_road(tile_type)
        self.__image = determine_image(tile_type)
        self.__angle = angle

    def is_road(self):
        """
        Getter for if the tile is a road or not.
        :return: Whether the tile is a type of road or not as a boolean
        """
        return self.__is_road

    def get_image(self):
        """
        Getter for the image of the tile.
        :return: The image of the tile as an image object
        """
        return self.__image

    def get_angle(self):
        """
        Getter for the angle for the image to be rotated by.
        :return: The angle for the image to be rotated by as an integer
        """
        return self.__angle


def determine_road(tile_type):
    """
    Function to determine whether the tile is a road or not
    :param tile_type: The name of the type of tile
    :return: Boolean which is true when the tile is a road, otherwise it is false
    """
    if tile_type == TileType.STRAIGHT_ROAD or tile_type == TileType.CORNER_ROAD or tile_type == TileType.T_JUNCTION or tile_type == TileType.CROSSROADS or tile_type == TileType.DEAD_END:
        return True
    else:
        return False


def determine_image(tile_type):
    """
    Function to return the corresponding image of a tile based on its name
    :param tile_type: The name of the type of tile
    :return:
    """
    if tile_type == TileType.STRAIGHT_ROAD:
        return image.load(".\\Images\\Roads\\straight.png")
    elif tile_type == TileType.CORNER_ROAD:
        return image.load(".\\Images\\Roads\\corner.png")
    elif tile_type == TileType.T_JUNCTION:
        return image.load(".\\Images\\Roads\\t_junction.png")
    elif tile_type == TileType.CROSSROADS:
        return image.load(".\\Images\\Roads\\crossroads.png")
    elif tile_type == TileType.DEAD_END:
        return image.load(".\\Images\\Roads\\dead_end.png")
    elif tile_type == TileType.DIRT:
        return image.load(".\\Images\\Terrain\\dirt.png")
    elif tile_type == TileType.GRASS:
        return image.load(".\\Images\\Terrain\\grass.png")
    elif tile_type == TileType.COFFEE_SHOP:
        return image.load(".\\Images\\Terrain\\coffee_shop.png")
    elif tile_type == TileType.LIBRARY:
        return image.load(".\\Images\\Terrain\\library.png")
    elif tile_type == TileType.CHURCH:
        return image.load(".\\Images\\Terrain\\church.png")
    elif tile_type == TileType.SWEET_SHOP:
        return image.load(".\\Images\\Terrain\\sweet_shop.png")
    elif tile_type == TileType.CANDY_SHOP:
        return image.load(".\\Images\\Terrain\\candy_shop.png")
    elif tile_type == TileType.FOOTBALL_CLUB:
        return image.load(".\\Images\\Terrain\\football_club.png")
    elif tile_type == TileType.HELIPAD:
        return image.load(".\\Images\\Terrain\\helipad.png")
    elif tile_type == TileType.JAIL:
        return image.load(".\\Images\\Terrain\\jail.png")
    elif tile_type == TileType.JEWELLERY_SHOP:
        return image.load(".\\Images\\Terrain\\jewellery_shop.png")
    elif tile_type == TileType.GAME_SHOP:
        return image.load(".\\Images\\Terrain\\game_shop.png")
    elif tile_type == TileType.BUS_STOP:
        return image.load(".\\Images\\Terrain\\bus_stop.png")


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
