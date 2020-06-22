from ShuttleBus import ShuttleBus


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


if __name__ == '__main__':
    print('Please save your instructions as "instructions.txt" and run run.py')
    input('Press any enter to close window . . . ')
