"""
Component 1 - collect_ingredients function
V1 - Collect ingredient names and store in list
V2 - Collect all ingredient info and store in list
V3 - Create class for each ingredient and store ingredient information in a list for each ingredient
V4 - Move code from Main into function
"""


class Ingredient:
    def __init__(self, name, needed, purchased, cost):
        self.name = name
        self.needed = needed
        self.purchased = purchased
        self.cost = cost


def collect_ingredients(num_of_ingredients):

    # Set up lists
    ingredient_lst = []

    # Check that the not blank function is called
    for i in range(num_of_ingredients):

        ingredient_name = input("What is ingredient {}'s name: ".format(i+1))

        amount_needed = input("How much {} in grams do you need in the recipe: ".format(ingredient_name))

        amount_purchased = input("How many grams of {} have you purchased: ".format(ingredient_name))

        cost_of_purchased = input("How much did the {} grams of {} cost: $ "
                                  .format(amount_purchased, ingredient_name))

        ingredient = Ingredient(ingredient_name, amount_needed, amount_purchased, cost_of_purchased)
        ingredient_lst.append(ingredient)
    return ingredient_lst


# Main

num_ingredients = 2
ingredient_list = collect_ingredients(num_ingredients)
for i in ingredient_list:
    print(f"{i.name}, {i.needed}, {i.purchased}, {i.cost}")
