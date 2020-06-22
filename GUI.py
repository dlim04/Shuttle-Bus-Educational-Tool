from ShuttleBus import ShuttleBus


def gui(program):
    code = program.get_code()
    shuttle_bus = ShuttleBus()
    for line in code:
        print(shuttle_bus.move(line))

    input('Press enter to close window . . . ')


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
