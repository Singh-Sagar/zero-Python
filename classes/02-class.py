class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)


restaurant1  = Restaurant("McD","fastfood")
print(restaurant1.restaurant_name)
restaurant1.describe_restaurant()