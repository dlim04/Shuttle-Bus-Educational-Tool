from common.ShuttleBus import ShuttleBus
from common.LoadFiles import load_map
from pygame import *


def gui(program):
    """
    Function to handle the graphical display of the shuttle bus program
    :param program: The compiled program generated from what the user has written
    """
    if not program.is_lexically_correct() or not program.is_compiled_correct():
        print("There was an error found in the program")
        print(program.get_error_message())
    else:
        animation(program)

    input('Press enter to close window . . . ')


def animation(program):
    """
    Function to animate the shuttle bus moving around the map grid
    :param program: The compiled program generated from what the user has written
    :return:
    """
    code = program.get_code()
    clock = time.Clock()
    init()
    display.set_caption("Shuttle Bus Educational Tool")
    window_size = (480, 480)
    screen = display.set_mode(window_size, 0, 32)
    tile_size = 32
    tile_map = load_map()
    shuttle_bus = ShuttleBus()
    bus_rect = Rect(shuttle_bus.get_x() * tile_size, shuttle_bus.get_y() * tile_size, tile_size, tile_size)
    tile_rects = []
    no_collision = True

    # Loop to add a Rect to all tiles which are not a type of road
    y = 0
    for row in tile_map:
        x = 0
        for tile in row:
            if not tile.is_road():
                tile_rects.append(Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1
        y += 1

    # Loop to execute each command given to the shuttle bus in sequence
    for line in code:
        draw_map(tile_map, screen, tile_size, shuttle_bus)
        for rects in tile_rects:
            if rects.colliderect(bus_rect):
                no_collision = False
                break

        if no_collision:
            clock.tick(2)
            display.update()
            print(shuttle_bus.move(line))
            bus_rect.x = shuttle_bus.get_x() * tile_size
            bus_rect.y = shuttle_bus.get_y() * tile_size
        else:
            break

    # If statement to display the final frame of animation if no collision has been detected
    if no_collision:
        draw_map(tile_map, screen, tile_size, shuttle_bus)
        clock.tick(2)
        display.update()
        print("The shuttle bus has reached it's destination!")
    else:
        print("Shuttle bus crashed!")


def draw_map(tile_map, screen, tile_size, shuttle_bus):
    """
    Function to draw the map on to the screen
    :param tile_map: The list of all tiles to be drawn on to the screen
    :param screen: The screen object which will e displayed
    :param tile_size: The height and width in pixels of the tiles
    :param shuttle_bus: The bus object which will move around the map grid
    """
    bus_img = image.load(".\\Images\\Bus\\bus.png").convert()
    bus_img.set_colorkey((255, 255, 255))

    y = 0
    for row in tile_map:
        x = 0
        for tile in row:
            screen.blit(transform.rotate(tile.get_image(), tile.get_angle()), (x * tile_size, y * tile_size))
            x += 1
        y += 1

    screen.blit(transform.rotate(bus_img, shuttle_bus.get_angle()),
                (shuttle_bus.get_x() * tile_size, shuttle_bus.get_y() * tile_size))


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
