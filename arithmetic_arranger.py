def arithmetic_arranger(problems, display_answers=False):
    # Error handling for too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""
