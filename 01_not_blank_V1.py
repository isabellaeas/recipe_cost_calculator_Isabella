"""
Component 1 - not blank function
V1 -  Checking to see that function is called. Returns a basic error message
"""


def not_blank(question):
    valid = False

    while not valid:
        answer = input(question)

        if answer != "":
            return answer
        else:
            print("Error")


# Main
# Check that the not blank function is called
recipe_name = not_blank("Name of the recipe: ")
