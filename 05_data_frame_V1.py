"""
V1 - Set up basic dataframe
"""

# Import statements
import pandas

# State variables
recipe_name = "Fritters"
serving_size = 3
total_cost = 7.96
cost_per_serving = 2.65

# Set data
data = {'Name': ['zucchini', 'carrot'],
        'Amount needed': [680, 600],
        'Price': [6, 4],
        'Amount purchased': [900, 700],
        'Cost to make': [4.53, 3.43]
        }

recipe_ingredients = pandas.DataFrame(data)

# Output
print("Recipe: ", recipe_name)
print("Servings: ", serving_size)
print()
print("Recipe ingredients")
print(recipe_ingredients)
print()
print("Total cost: ", total_cost)
print("Per serving: ", cost_per_serving)
