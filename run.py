from Analyzer import analyzer
from CompiledProgram import CompiledProgram
from Compiler import compiler
from GUI import gui
from LoadFiles import load_instructions, load_settings
from TokenType import TokenType
from Tokenizer import tokenizer


def main():
    settings = load_settings()
    program = load_instructions(settings.get_instructions_filename())
    tokenized_program = tokenizer(program)
    analysis = analyzer(tokenized_program)
    if analysis is not None:
        compiled_program = CompiledProgram(False, False, analysis, None)
    else:
        compiler_output = compiler(tokenized_program, settings.get_logical_loop_limit())
        if compiler_output == TokenType.ERROR_LOGICAL_ERROR:
            compiled_program = CompiledProgram(True, False, "Logical error found: Infinite loop created", None)
        else:
            compiled_program = CompiledProgram(True, True, None, compiler_output)

    gui(compiled_program)


if __name__ == '__main__':
    main()