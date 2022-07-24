"""
Component 2 - int checker function
V1 -  Checking to see that function is called. Returns a basic error message
"""


def currency_checker(question, error_message):

    while True:
        try:
            answer = float(input(question))
            if answer <= 0:
                print(error_message)
            else:
                return answer

        except:
            print(error_message)


# Main
amount_purchased = 900
ingredient_name = "zucchini"

cost_of_purchased = currency_checker("How much did the {} grams of {} cost: $"
                                     .format(amount_purchased, ingredient_name),
                                     "Sorry this is not an valid price, please enter how much it cost")
