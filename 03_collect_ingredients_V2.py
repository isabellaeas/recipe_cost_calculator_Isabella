"""
Component 1 - collect_ingredients function
V1 -  Collect ingredient names and store in list
V2 -  Collect all ingredient info and store in list
"""


def collect_ingredients(question):
    answer = input(question)
    ingredient_lst.append(answer)
    return answer


# Main
# Set up lists
ingredient_lst = []

num_of_ingredients = 5

# Check that the not blank function is called
for i in range(num_of_ingredients):

    # Ask for ingredient name
    ingredient_name = collect_ingredients("What is ingredient {}'s name: ".format(i+1))

    # Ask for amount of ingredient needed
    amount_needed = collect_ingredients("How much {} in grams do you need in the recipe: ".format(ingredient_name))

    # Ask for amount of ingredient purchased
    amount_purchased = collect_ingredients("How many grams of {} have you purchased: ".format(ingredient_name))

    # Ask for cost of purchased ingredient
    cost_of_purchased = collect_ingredients("How much did the {} grams of {} cost: $"
                                            .format(amount_purchased, ingredient_name))

    # Print list of ingredients
    print(ingredient_lst)
