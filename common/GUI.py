from common.ShuttleBus import ShuttleBus
from common.Tile import *
from common.LoadFiles import load_map
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

    tile_map = load_map()

    while True:
        y = 0
        for line in tile_map:
            x = 0
            for tile in line:
                screen.blit(transform.rotate(tile.get_image(), tile.get_angle()), (x * 32, y * 32))
                x += 1
            y += 1

        display.update()
        clock.tick(30)


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    animation("Test")
    input('Press enter to close window . . . ')
