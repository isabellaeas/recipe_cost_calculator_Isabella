"""
Component 1 - not blank function
V1 -  Checking to see that function is called. Returns a basic error message
V2 - Add 'error_message' parameter so function works for more outcomes
"""


def not_blank(question, error_message):
    valid = False

    while not valid:
        answer = input(question)

        if answer != "":
            return answer
        else:
            print(error_message)


# Main
# Check that the not blank function is called
recipe_name = not_blank("Recipe name:",
                        "sorry this can't be blank, "
                        "please enter you recipe's name")
