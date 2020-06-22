from Function import Function
from Loop import Loop
from TokenType import *


def compiler(instructions, logical_loop_limit):
    """
    Function to compile the instructions to be read by the shuttle bus.
    :param logical_loop_limit: The loop limit before the compiler returns an error as an integer
    :param instructions: The instructions in a tokenized form
    :return: The program to be run by the shuttle bus
    """
    # Remove blank lines
    while [] in instructions:
        instructions.remove([])

    # Remove semicolons
    for line in instructions:
        while TokenType.SEMICOLON in line:
            line.remove(TokenType.SEMICOLON)

    if compile_functions(instructions, logical_loop_limit) == TokenType.ERROR_LOGICAL_ERROR:
        return TokenType.ERROR_LOGICAL_ERROR

    compile_loops(instructions)

    # Remove parenthesis
    for line in instructions:
        while TokenType.LEFT_PAREN in line:
            line.remove(TokenType.LEFT_PAREN)

        while TokenType.RIGHT_PAREN in line:
            line.remove(TokenType.RIGHT_PAREN)

    return instructions


def compile_functions(instructions, logical_loop_limit):
    """
    Helper procedure to to replace function calls with their declarations
    :param logical_loop_limit: The loop limit before the compiler returns an error as an integer
    :param instructions: A pointer to the instructions being stored as a 2D array
    """
    # Replace function calls with declarations
    functions, loops = find_scopes(instructions)

    # Remove Function declarations
    line_count = 0
    for function in functions:
        function_declaration_start = function.get_line_number() - line_count - 1
        for i in range(0, function.get_length() + 2):
            line_count += 1
            instructions.pop(function_declaration_start)

    while has_function_call(instructions):
        # Replace function calls with functions
        for function in functions:
            program_line = 0

            loop_count = 0
            for line in instructions:
                loop_count += 1
                if loop_count == logical_loop_limit:
                    return TokenType.ERROR_LOGICAL_ERROR
                program_line += 1
                if line[0] == function.get_name():
                    instructions.remove(line)

                    function_line = 0
                    for i in range(program_line - 1, function.get_length() + program_line - 1):
                        function_line += 1
                        instructions.insert(i, function.get_instructions()[function_line - 1])


def compile_loops(instructions):
    """
    Helper procedure to expand out the loops in instructions.
    :param instructions: A pointer to the instructions being stored as a 2D array
    """
    while has_loop(instructions):
        # Expand out for loops
        functions, loops = find_scopes(instructions)
        lines_added = 0
        for loop in loops:
            loop_start = loop.get_line_number() - 1 + lines_added
            loop_end = loop.get_length() + 2 + loop_start
            del instructions[loop_start:loop_end]
            lines_added -= loop.get_length() + 2

            expanded_loop = loop.expand()
            loop_line = 0
            for i in range(loop_start, loop_start + len(expanded_loop)):
                lines_added += 1
                instructions.insert(i, expanded_loop[loop_line])
                loop_line += 1


def find_scopes(instructions):
    """
    Function to find all the outer scopes in a set of instructions.
    :param instructions: The instructions to be checked for scopes
    :return: A 2d array holding a list of functions and a list of loops
    """
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

        line_number += current_scope.get_length() + 2

        current_scope = find_scope(instructions_copy, line_number)

    return functions, loops


def find_scope(snippet, snippet_start):
    """
    Function to find the first outer scope in a given code snippet.
    :param snippet: A section of code for the first scope to be found in as a 2D list
    :param snippet_start: The line number of the larger program the snippet starts at as an integer
    :return: A scope object containing the information about the scope
    """
    left_brace_count = 0
    right_brace_count = 0
    scope_found = False
    scope_complete = False

    line_count = 0
    scope_start = 0
    scope_end = 0

    for line in snippet:
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

    scope = snippet[(scope_start - 1):scope_end]

    if len(scope) != 0:
        if scope[0][0] == TokenType.KEYWORD_FUNCTION:
            return Function(snippet_start + scope_start - 1, scope)

        elif scope[0][0] == TokenType.KEYWORD_FOR:
            return Loop(snippet_start + scope_start - 1, scope)


def has_function_call(instructions):
    """
    A function to determine whether the instruction contain any calls to any functions.
    :param instructions: The instructions to check for function calls
    :return: Whether the instructions contain any calls to any functions as a boolean value
    """
    for line in instructions:
        for each in line:
            if type(each) == str:
                return True
    return False


def has_loop(instructions):
    """
    A function to determine whether the instruction contain any loops.
    :param instructions: The instructions to check for loops
    :return: Whether the instructions contain any calls to any functions as a boolean value
    """
    for line in instructions:
        for each in line:
            if each == TokenType.KEYWORD_FOR:
                return True
    return False


if __name__ == '__main__':
    print('Please save your instructions and run run.py')
    input('Press enter to close window . . . ')
