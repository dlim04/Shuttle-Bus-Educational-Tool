import ShuttleBus


def animation(program):
    for line in program:
        print(ShuttleBus.move(line))


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run RunInstructions.py')
    input('Press any enter to close window . . . ')
