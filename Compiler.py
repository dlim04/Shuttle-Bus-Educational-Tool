from Function import Function
from Loop import Loop
from TokenType import *


def compiler(instructions):

    # Remove blank lines
    while [] in instructions:
        instructions.remove([])

    # Remove semicolons
    for line in instructions:
        while TokenType.SEMICOLON in line:
            line.remove(TokenType.SEMICOLON)

    functions, loops = find_scopes(instructions)

    # Remove Function declarations
    line_count = 0
    for function in functions:
        function_declaration_start = function.get_line_number() - line_count - 1
        for i in range(0, function.get_length() + 2):
            line_count += 1
            instructions.pop(function_declaration_start)
        line_count -= 2

    # Replace function calls with functions
    for function in functions:
        program_line = 0
        for line in instructions:
            program_line += 1
            if line[0] == function.get_name():
                instructions.remove(line)

                function_line = 0
                for i in range(program_line - 1, function.get_length() + program_line - 1):
                    function_line += 1
                    instructions.insert(i, function.get_instructions()[function_line - 1])

    return instructions


def find_scopes(instructions):
    instructions_copy = instructions.copy()
    line_number = 1
    functions = []
    loops = []

    current_scope = find_scope(instructions_copy, line_number)

    while current_scope is not None:
        if current_scope.get_type() == TokenType.SCOPE_FUNCTION:
            functions.append(current_scope)

        elif current_scope.get_type() == TokenType.SCOPE_LOOP:
            loops.append(current_scope)

        for i in range(0, current_scope.get_length() + 2):
            instructions_copy.pop(current_scope.get_line_number() - line_number)

        line_number += current_scope.get_length()

        current_scope = find_scope(instructions_copy, line_number)

    return functions, loops


def find_scope(program, snippet_start):
    left_brace_count = 0
    right_brace_count = 0
    scope_found = False
    scope_complete = False

    line_count = 0
    scope_start = 0
    scope_end = 0

    for line in program:
        line_count += 1

        for each in line:
            if each == TokenType.LEFT_BRACE and not scope_found:
                scope_start = line_count
                scope_found = True

            elif each == TokenType.LEFT_BRACE:
                left_brace_count += 1

            elif each == TokenType.RIGHT_BRACE:
                right_brace_count += 1

            if left_brace_count + 1 == right_brace_count:
                scope_end = line_count
                scope_complete = True
                break

        if scope_complete:
            break

    scope = program[(scope_start - 1):scope_end]

    if len(scope) != 0:
        if scope[0][0] == TokenType.KEYWORD_FUNCTION:
            return Function(snippet_start + scope_start - 1, scope)

        elif scope[0][0] == TokenType.KEYWORD_FOR:
            return Loop(snippet_start + scope_start - 1, scope)


"""
Sample
output = [[TokenType.SPECIAL_FORWARD, 1],
          [TokenType.SPECIAL_LEFT, 90],
          [TokenType.SPECIAL_FORWARD, 1],
          [TokenType.SPECIAL_LEFT, 90],
          [TokenType.SPECIAL_FORWARD, 1],
          [TokenType.SPECIAL_LEFT, 90],
          [TokenType.SPECIAL_FORWARD, 1]]
"""