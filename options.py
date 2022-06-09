# creation:

meat = ["Steak", "Chicken Breast", "Bifana"]
fish = ["Codfish", "Sardines"]
side_dish = ["Veggies", "Rice", "French Fries"]

cooking = ["grilled", "fried", "Steamed"]

class Food:

    def take_away(self):
        print("To take away.")

    def on_site(self):
        print("To eat here.")


class Meat(Food):

    def grilled(self):
        print("grilled")


class Fish(Food):
    pass


class Side_dish(Food):
    pass


class cooking:
    pass
