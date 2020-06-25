from common.ShuttleBus import ShuttleBus
from common.LoadFiles import load_map
from pygame import *


def gui(program):
    if not program.is_lexically_correct() or not program.is_compiled_correct():
        print("There was an error found in the program")
        print(program.get_error_message())
    else:
        code = program.get_code()
        shuttle_bus = ShuttleBus()
        animation(shuttle_bus)
        for line in code:
            print(shuttle_bus.move(line))
            animation(shuttle_bus)

    input('Press enter to close window . . . ')


def animation(shuttle_bus):
    clock = time.Clock()
    init()
    display.set_caption("Shuttle Bus Educational Tool")
    window_size = (480, 480)
    screen = display.set_mode(window_size, 0, 32)
    tile_size = 32
    tile_map = load_map()
    bus_img = image.load(".\\Images\\Bus\\bus.png").convert()
    bus_img.set_colorkey((255, 255, 255))

    y = 0
    for line in tile_map:
        x = 0
        for tile in line:
            screen.blit(transform.rotate(tile.get_image(), tile.get_angle()), (x * tile_size, y * tile_size))
            x += 1
        y += 1

    screen.blit(transform.rotate(bus_img, shuttle_bus.get_angle()), (shuttle_bus.get_x() * tile_size, shuttle_bus.get_y() * tile_size))

    display.update()
    clock.tick(2)


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
