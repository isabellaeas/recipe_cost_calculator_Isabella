"""
Component 2 - int checker function
V1 -  Checking to see that function is called. Returns a basic error message
"""


def int_checker(question, error_message):

    while True:
        try:
            answer = int(input(question))
            if answer < 1:
                print(error_message)
            else:
                return answer

        except:
            print(error_message)


# Main
# Check that the not blank function is called
serving_size = int_checker("Serving size:",
                           "sorry this is not an integer, "
                           "please enter your serving size")
