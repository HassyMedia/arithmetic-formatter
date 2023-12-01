def arithmetic_arranger(problems, display_answers=False):
    # Error handling for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for index, problem in enumerate(problems):
        # Splitting each problem into parts
        parts = problem.split()
        # Error handling for invalid problem format
        if len(parts) != 3:
            return "Error: Invalid problem format."

        first_number, operator, second_number = parts

        # Ensuring correct operator and digit-only operands
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (first_number.isdigit() and second_number.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check for operand length
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
