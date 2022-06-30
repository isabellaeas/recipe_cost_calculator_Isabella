"""
Component 1 - collect_ingredients function
V1 -  Collect ingredient names and store in list
"""


def collect_ingredients(question):
    for i in range(num_of_ingredients):
        answer = input(question)
        ingredient_lst.append(answer)

    print(ingredient_lst)
    return answer


# Main
ingredient_lst = []

num_of_ingredients = 5
count = 1

ingredient_name = collect_ingredients("Name of ingredient:")
