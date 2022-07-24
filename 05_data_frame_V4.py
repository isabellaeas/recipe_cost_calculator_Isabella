"""
V1 - Set up basic dataframe
V2 - Pass in real data
V3 - Column titles an
V4 - Make dataframe clear and visually appealing
"""

# Import statements
import pandas
from tabulate import tabulate

# State variables
recipe_name = "Fritters"
serving_size = 3
total_cost = 7.96
cost_per_serving = 2.65

# Set up lists
real_data = []


# Real data
class Ingredient:
    def __init__(self, name, needed, purchased, cost):
        self.name = name
        self.needed = needed
        self.purchased = purchased
        self.cost = cost


real_data.append(Ingredient("zucchini", 680, 900, 6))
real_data.append(Ingredient("carrot", 600, 700, 4))

# Set up dataframe
recipe_ingredients = pandas.DataFrame([vars(i) for i in real_data])

# Change column names
recipe_ingredients.columns = ["Ingredient", "Amount needed", "Amount purchased", "Price"]

# Calculate cost to make
recipe_ingredients["Cost to make"] = \
        (recipe_ingredients["Price"] / recipe_ingredients["Amount purchased"] * recipe_ingredients["Amount needed"])\

# Format data
recipe_ingredients["Price"] = recipe_ingredients["Price"].apply("${:,.2f}".format)
recipe_ingredients["Cost to make"] = recipe_ingredients["Cost to make"].apply("${:,.2f}".format)
recipe_ingredients["Amount needed"] = recipe_ingredients["Amount needed"].apply("{} grams".format)
recipe_ingredients["Amount purchased"] = recipe_ingredients["Amount purchased"].apply("{} grams".format)

# Output
print("Recipe: ", recipe_name)
print("Servings: ", serving_size)
print()
print("Recipe ingredients")
print(tabulate(recipe_ingredients, headers='keys', tablefmt='pretty',))
print()
print("Total cost: ", "${:,.2f}".format(total_cost))
print("Per serving: ", "${:,.2f}".format(cost_per_serving))
