from common.ShuttleBus import ShuttleBus
from common.Tile import *
from common.TileType import TileType
from pygame import *


def gui(program):
    if not program.is_lexically_correct() or not program.is_compiled_correct():
        print("There was an error found in the program")
        print(program.get_error_message())
    else:
        code = program.get_code()
        shuttle_bus = ShuttleBus()
        for line in code:
            print(shuttle_bus.move(line))

    input('Press enter to close window . . . ')


def animation(program):
    clock = time.Clock()
    init()
    display.set_caption("Shuttle Bus Educational Tool")
    window_size = (480, 480)
    screen = display.set_mode(window_size, 0, 32)

    tile_map = [[[TileType.CORNER_ROAD, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CORNER_ROAD, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.FOOTBALL_CLUB, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.COFFEE_SHOP, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.CANDY_SHOP, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.LIBRARY, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.LIBRARY, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.CHURCH, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.SWEET_SHOP, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.T_JUNCTION, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.CROSSROADS, 0], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 270]],
                [[TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0], [TileType.GRASS, 0], [TileType.STRAIGHT_ROAD, 0]],
                [[TileType.CORNER_ROAD, 90], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.T_JUNCTION, 180], [TileType.STRAIGHT_ROAD, 90], [TileType.CORNER_ROAD, 180]]]

    while True:
        y = 0
        for layer in tile_map:
            x = 0
            for tile in layer:
                tile_displayed = Tile(tile[0], tile[1])
                screen.blit(transform.rotate(tile_displayed.get_image(), tile_displayed.get_angle()), (x * 32, y * 32))
                x += 1
            y += 1

        display.update()
        clock.tick(30)


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
