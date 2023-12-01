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

        # Arranging each problem
        longest_operand = max(len(first_number), len(second_number))
        total_length = longest_operand + 2
        top_number = first_number.rjust(total_length)
        bottom_number = operator + second_number.rjust(total_length - 1)
        dashes = '-' * total_length

        # Adding spacing between problems
        if index > 0:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            answers_line += "    "

        first_line += top_number
        second_line += bottom_number
        dashes_line += dashes

        # Calculating and displaying answers if requested
        if display_answers:
            answer = ""
            if operator == '+':
                answer = str(int(first_number) + int(second_number)).rjust(total_length)
            else:
                answer = str(int(first_number) - int(second_number)).rjust(total_length)
            answers_line += answer

    # Forming the final arranged string
    if display_answers:
        arranged_problems = "\n".join([first_line, second_line, dashes_line, answers_line])
    else:
        arranged_problems = "\n".join([first_line, second_line, dashes_line])

    return arranged_problems


