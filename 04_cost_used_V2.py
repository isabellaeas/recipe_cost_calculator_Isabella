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
zucchini = Ingredient('Zucchini', 680, 900, 6)
carrot = Ingredient('Carrot', 600, 700, 4)

print(zucchini.cost_used(), carrot.cost_used())
