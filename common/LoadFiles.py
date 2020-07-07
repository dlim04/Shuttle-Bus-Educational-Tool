import csv
import io
import re

from common.Settings import Settings
from common.Tile import Tile
from common.TileType import string_to_tile_type
from pygame.rect import Rect


def load_instructions(filename):
    """
    Function to read a string in from a text file and return that string.
    :param filename: The name of the text file as a string
    :return: The contents of the text file as a string
    """
    filepath = ".\\" + filename
    try:
        file = open(filepath)
    except FileNotFoundError:
        file = open(filepath, "x")

    try:
        program = file.read()
        file.close()
    except io.UnsupportedOperation:
        program = ""

    return program


def load_settings():
    """
    Function to read the settings file and return a settings object that stores the settings specified in the
    Settings.txt.
    :return: The Settings object that stores the settings for the compiler
    """
    settings_file = ".\\Settings.txt"
    try:
        file = open(settings_file)
        settings_string = file.read()
    except FileNotFoundError:
        settings_string = ""

    settings = Settings(settings_string)

    return settings


def load_map(tile_size):
    """
    Procedure to read a map from a file.
    :param tile_size: The height and width in pixels of the tiles
    :return: A nested list of Tile objects, a nested list of all tile rects on the map
    """
    map_file = ".\\Map.csv"
    map_list = []
    map_rects = []
    reader = csv.reader(open(map_file), delimiter=";")
    y = 0
    for row in reader:
        x = 0
        map_line = []
        for tile in row:
            tile_values = re.split(',', tile)
            for i in range(0, len(tile_values)):
                tile_values[i] = tile_values[i].replace(' ', '')
            current_tile = Tile(string_to_tile_type(tile_values[0]), int(tile_values[1]))
            map_line.append(current_tile)
            if not current_tile.is_road():
                map_rects.append(Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1
        map_list.append(map_line)
        y += 1
    return map_list, map_rects


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
