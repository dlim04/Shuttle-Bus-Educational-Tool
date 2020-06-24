from common.Analyzer import analyzer
from common.CompiledProgram import CompiledProgram
from common.Compiler import compiler
from common.GUI import gui
from common.LoadFiles import load_instructions, load_settings
from common.TokenType import TokenType
from common.Tokenizer import tokenizer


def main():
    settings = load_settings()
    program = load_instructions(settings.get_instructions_filename())
    tokenized_program = tokenizer(program)
    analysis = analyzer(tokenized_program)
    if analysis is not None:
        compiled_program = CompiledProgram(False, False, analysis, 0, None)
    else:
        instructions_line_count, compiler_output = compiler(tokenized_program, settings.get_logical_loop_limit())
        if compiler_output == TokenType.ERROR_LOGICAL_ERROR:
            compiled_program = CompiledProgram(True, False, "Logical error found: Infinite loop created", 0, None)
        else:
            compiled_program = CompiledProgram(True, True, None, instructions_line_count, compiler_output)

    gui(compiled_program)


if __name__ == '__main__':
    main()
