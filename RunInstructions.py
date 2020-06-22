from CompiledProgram import CompiledProgram
from GUI import gui
from LoadInstructions import load_instructions
from Tokenizer import *
from Analyzer import *
from Compiler import *


def main():
    program = load_instructions("Instructions.txt")
    tokenized_program = tokenizer(program)
    analysis = analyzer(tokenized_program)
    if analysis is not None:
        compiled_program = CompiledProgram(False, False, analysis, None)
    else:
        compiler_output = compiler(tokenized_program)
        compiled_program = CompiledProgram(True, True, None, compiler_output)

    gui(compiled_program)


if __name__ == '__main__':
    main()