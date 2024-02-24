class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)


class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name, cuisine_type):
        # super().__init__(restaurant_name, cuisine_type)
        super().__init__(restaurant_name, cuisine_type)  # Corrected super() call
        self.flavors = ['strawberry', 'chocolate','vanilla','grapeberry']

    def display_flavors(self):
        """Displays ice-cream flavors available"""
        print("We have: ", end = "")
        for i in self.flavors:
            print(i,end = " ")
        print()

trentIce = IceCreamStand("trentIce","icecream")
trentIce.display_flavors()