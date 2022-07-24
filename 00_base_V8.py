"""
Program to calculate cost for recipe per serving
V1 - Set up skeleton of program
V2 - Add in not_blank function
V3 - Add in int_checker function
V3.1 - Ask user for num of ingredients
V4 - Add collect_ingredients function into base
V4.1 - Fix errors
V5 - Add cost_used into base
V6 - Calculate total cost and cost per serving
V7 - add dataframe into base
V8 - Make program visually appealing
"""

# Import statements
import pandas
from tabulate import tabulate


# Set up class

# Class to store ingredient
class Ingredient:
    def __init__(self, name, needed, purchased, cost):
        self.name = name
        self.needed = needed
        self.purchased = purchased
        self.cost = cost


# Set up functions

# Function to check if recipe name is blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        answer = input(question).strip()

        if answer != "":
            return answer
        else:
            print(error_message)


# Function to check for integers. Will loop until integer is input
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


# Function to collect information for each ingredient and put into lists
def collect_ingredients(number):

    # Set up lists
    ingredients = []

    # Check that the not blank function is called
    for i in range(number):

        # Ask for ingredient name
        ingredient_name = not_blank("What is ingredient {}'s name: ".format(i+1),
                                    "sorry this can't be blank, please enter the ingredient's name").title()

        # Ask for amount of ingredient needed
        amount_needed = int_checker("How much {} in grams do you need in the recipe: ".format(ingredient_name),
                                    "sorry this is not an valid integer, please enter the number grams needed")

        # Ask for amount of ingredient purchased
        amount_purchased = int_checker("How many grams of {} have you purchased: ".format(ingredient_name),
                                       "sorry this is not an valid integer, please enter the amount you have purchased")

        # Ask for cost of purchased ingredient
        cost_of_purchased = int_checker("How much did the {} grams of {} cost: $"
                                        .format(amount_purchased, ingredient_name),
                                        "sorry this is not an valid integer, please enter how much it cost")

        # Store in list
        ingredient = Ingredient(ingredient_name, amount_needed, amount_purchased, cost_of_purchased)
        ingredients.append(ingredient)
    return ingredients


# Set up main
if __name__ == "__main__":
    # Set up variables in main routine

    # Ask users for input
    print("****RECIPE COST CALCULATOR****")
    print()
    print("Welcome to the Recipe Cost Calculator")
    print("Please enter the following details")
    print()

    # Ask user for recipe name
    # Check not blank
    recipe_name = not_blank("Recipe name: ",
                            "sorry this can't be blank, "
                            "please enter your recipe's name").title()

    # Ask user for serving size
    # Int checker
    serving_size = int_checker("Serving size: ",
                               "sorry this is not a valid integer, "
                               "please enter your serving size")

    # Ask user for number of ingredients
    # Int checker
    num_of_ingredients = int_checker("Number of ingredients: ",
                                     "sorry this is not an valid integer, "
                                     "please enter the number of ingredients")
    # Loop for number of ingredients

    ingredient_list = collect_ingredients(num_of_ingredients)

    # Set up dataframe
    recipe_ingredients = pandas.DataFrame([vars(i) for i in ingredient_list])

    # Change column names
    recipe_ingredients.columns = ["Ingredient", "Amount needed", "Amount purchased", "Price"]

    # Calculate cost to make
    recipe_ingredients["Cost to make"] = \
        (recipe_ingredients["Price"] / recipe_ingredients["Amount purchased"] * recipe_ingredients["Amount needed"])

    # Calculate total cost
    total_cost = recipe_ingredients["Cost to make"].sum()
    cost_per_serving = total_cost / serving_size

    # Format data
    recipe_ingredients["Price"] = recipe_ingredients["Price"].apply("${:,.2f}".format)
    recipe_ingredients["Cost to make"] = recipe_ingredients["Cost to make"].apply("${:,.2f}".format)
    recipe_ingredients["Amount needed"] = recipe_ingredients["Amount needed"].apply("{} grams".format)
    recipe_ingredients["Amount purchased"] = recipe_ingredients["Amount purchased"].apply("{} grams".format)

    # Output
    print()
    print()
    print("Recipe: ", recipe_name)
    print("Servings: ", serving_size)
    print()
    print("Recipe ingredients")
    print(tabulate(recipe_ingredients, headers='keys', tablefmt='pretty', ))
    print()
    print("Total cost: ", "${:,.2f}".format(total_cost))
    print("Cost per serving: ", "${:,.2f}".format(cost_per_serving))
