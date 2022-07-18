"""
Component 4 - cost used function
V1 -  Calculate cost per amount of ingredient used for one ingredient
"""

cost_of_purchased = 6
amount_needed = 680
amount_purchased = 900

cost = (cost_of_purchased / amount_purchased * amount_needed)

print("{:.2f}". format(cost))
