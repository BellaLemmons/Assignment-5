### Data ###
from operator import truediv

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] >= ingredients["bread"]:
            return True
        elif self.machine_resources["ham"] >= ingredients["ham"]:
            return True
        elif self.machine_resources["cheese"] >= ingredients["cheese"]:
            return True
        else:
            print("Sorry! There's not enough resources to make your sandwich. :(")
            return False


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("Insert number of dollars: "))
        half_dollars = int(input("Insert number of half dollars: "))
        quarters = int(input("Insert number of quarters: "))
        nickels = int(input("Insert number of nickels: "))

        return dollars + (half_dollars * 0.5) + (quarters * 0.25) + (nickels * 0.05)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Payment accepted. Your change is $" + str(coins - cost) + ".")
            return True
        else:
            print("Payment rejected. Not enough money.")
            return False


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] = self.machine_resources["bread"] - order_ingredients["bread"]
        self.machine_resources["ham"] = self.machine_resources["ham"] - order_ingredients["ham"]
        self.machine_resources["cheese"] = self.machine_resources["cheese"] - order_ingredients["cheese"]
        print("Enjoy your " + str(sandwich_size) + " sandwich!")



### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_maker = SandwichMachine(resources) ##uses the global variable resources as parameter for the new machine class

user_input = str(input("What would you like? {small/medium/large/report/off} "))

while True:
    if user_input == "report":
        print("Bread: " + str(sandwich_maker.machine_resources["bread"]) + "\n")
        print("Ham: " + str(sandwich_maker.machine_resources["ham"]) + "\n")
        print("Cheese: " + str(sandwich_maker.machine_resources["cheese"]) + "\n")
        user_input = str(input("What would you like? {small/medium/large/report/off} "))
    elif user_input == "off":
        break
    else:
        sandwich_price = recipes[user_input]["cost"]
        sandwich_ingredients = recipes[user_input]["ingredients"]
        user_payment = sandwich_maker.process_coins()
        if sandwich_maker.check_resources(sandwich_ingredients):
            if sandwich_maker.transaction_result(user_payment, sandwich_price):
                sandwich_maker.make_sandwich(user_input, sandwich_ingredients)
        user_input = str(input("What would you like? {small/medium/large/report/off} "))
