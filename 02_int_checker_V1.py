"""
Component 2 - int checker function
V1 -  Checking to see that function is called. Returns a basic error message
"""


def int_checker(question):

    while True:
        try:
            answer = int(input(question))
            if answer < 1:
                print("Error")
            else:
                return answer

        except:
            print("Error")


# Main
# Check that the not blank function is called
serving_size = int_checker("Serving size:")
