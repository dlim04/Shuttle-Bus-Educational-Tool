from common.ShuttleBus import *
from common.LoadFiles import load_map
from common.TokenType import TokenType
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
    """
    code = program.get_code()
    clock = time.Clock()
    display.init()
    display.set_caption("Shuttle Bus Educational Tool")
    window_size = (480, 480)
    screen = display.set_mode(window_size, 0, 32)
    tile_size = 32
    tile_map = load_map()
    shuttle_bus = ShuttleBus()
    bus_rect = Rect(shuttle_bus.get_x() * tile_size, shuttle_bus.get_y() * tile_size, tile_size, tile_size)
    tile_rects = []

    # Loop to add a Rect to all tiles which are not a type of road
    y = 0
    for row in tile_map:
        x = 0
        for tile in row:
            if not tile.is_road():
                tile_rects.append(Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1
        y += 1

    draw_map(clock, tile_map, screen, tile_size, shuttle_bus)

    # Loop to execute each command given to the shuttle bus in sequence
    for line in code:
        allow_exit()
        if line[0] == TokenType.SPECIAL_FORWARD or line[0] == TokenType.SPECIAL_REVERSE:
            # Loop to animate the shuttle bus moving forwards or reversing while checking for collisions
            for i in range(0, 16 * line[1]):
                allow_exit()
                if not collision_check(tile_rects, bus_rect):
                    if line[0] == TokenType.SPECIAL_FORWARD:
                        shuttle_bus.drive(2 / tile_size)
                    else:
                        shuttle_bus.drive(-2 / tile_size)
                    bus_rect.x = shuttle_bus.get_x() * tile_size
                    bus_rect.y = shuttle_bus.get_y() * tile_size
                    draw_map(clock, tile_map, screen, tile_size, shuttle_bus)
                else:
                    break

            if collision_check(tile_rects, bus_rect):
                break

        else:
            # Loop to animate the shuttle bus turning right or left (collisions cannot occur when turning)
            for i in range(0, int(line[1] / 5)):
                allow_exit()
                if line[0] == TokenType.SPECIAL_LEFT:
                    shuttle_bus.left(5)
                else:
                    shuttle_bus.right(5)
                draw_map(clock, tile_map, screen, tile_size, shuttle_bus)

        # Print the instruction completed to the console, provided the shuttle bus did not crash
        print(move(line))

    # If statement to print a line of text to at the end of the bus journey
    if not collision_check(tile_rects, bus_rect):
        print("The shuttle bus has reached it's destination!")
    else:
        print("Shuttle bus crashed!")

    while True:
        allow_exit()


def draw_map(clock, tile_map, screen, tile_size, shuttle_bus):
    """
    Function to draw the map on to the screen
    :param clock: The internal clock the game runs on
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

    bus_img_rotated = transform.rotate(bus_img, shuttle_bus.get_angle())
    screen.blit(bus_img_rotated,
                (shuttle_bus.get_x() * tile_size + int(bus_img.get_width() / 2) - int(bus_img_rotated.get_width() / 2),
                 shuttle_bus.get_y() * tile_size + int(bus_img.get_height() / 2) - int(bus_img_rotated.get_height() / 2)))
    clock.tick(30)
    display.update()


def collision_check(tile_rects, bus_rect):
    """
    Function to check for bus collisions
    :param tile_rects: The list of all tile rects on the map
    :param bus_rect: The rect of the shuttle bus
    :return: Whether there is a collision or not as a boolean value
    """
    for rects in tile_rects:
        if rects.colliderect(bus_rect):
            return True
    return False


def allow_exit():
    """
    Function to allow exiting the pygame window and closing the program
    """
    for events in event.get():
        if events.type == QUIT:
            display.quit()
            exit()


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
