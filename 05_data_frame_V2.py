"""
V1 - Set up basic dataframe
V2 - Pass in real data
"""

# Import statements
import pandas

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


recipe_ingredients = pandas.DataFrame([vars(i) for i in real_data])

# Calculate cost per ingredient used
recipe_ingredients["Cost to make"] = \
        (recipe_ingredients["cost"] / recipe_ingredients["purchased"] * recipe_ingredients["needed"])\
        .round(2)


# Output
print("Recipe: ", recipe_name)
print("Servings: ", serving_size)
print()
print("Recipe ingredients")
print(recipe_ingredients)
print()
print("Total cost: ", total_cost)
print("Per serving: ", cost_per_serving)
