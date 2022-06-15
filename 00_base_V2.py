"""
Program to calculate cost for recipe per serving
V1 - Set up skeleton of program
V2 - add in not_blank function
"""


# Set up functions

# Function to check if recipe name is blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        answer = input(question)

        if answer != "":
            return answer
        else:
            print(error_message)


# Function to check for integers. Will loop until integer is input
def int_checker():
    print("placeholder")


# Function to calculate cost per amount
def cost_calculator():
    print("placeholder")


# Set up lists and constants
ingredient_lst = []
amount_needed_lst = []
amount_purchased_lst = []
price_lst = []

# Set up main
if __name__ == "__main__":
    # Set up variables in main routine

    # Ask users for input
    print("****RECIPE COST CALCULATOR****")
    print()
    print("Welcome to the recipe cost calculator")

    # Ask user for recipe name
    # Check not blank
    recipe_name = not_blank("Recipe name:",
                            "sorry this can't be blank, "
                            "please enter you recipe's name")

    # Ask user for serving size
    # Int checker

    # Ask user for number of ingredients
    # Int checker

    # Loop for number of ingredients

    # Ask for ingredient
    # Ask for amount needed
    # Ask for amount purchased
    # Ask for price of amount purchased

    # Output information
