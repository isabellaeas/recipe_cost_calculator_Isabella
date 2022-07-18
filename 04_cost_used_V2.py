"""
Component 4 - cost used function
V1 -  Calculate cost per amount of ingredient used for one ingredient
V2 -  Add function into class to calculate for all ingredients
"""

class Ingredient:
    def __init__(self, name, needed, purchased, cost):
        self.name = name
        self.needed = needed
        self.purchased = purchased
        self.cost = cost

    def cost_used(self):
        return self.cost / self.purchased * self.needed


# Main
flour = Ingredient('Flour', 200, 500, 5)
ing2 = Ingredient('Chicken', 100, 200, 3)

print(ing2.cost_used())


