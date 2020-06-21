from ShuttleBus import ShuttleBus


def animation(program):
    shuttle_bus = ShuttleBus()
    for line in program:
        print(shuttle_bus.move(line))


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
