
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update(self, mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size = 75):
        """initialize the battery's attribute"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        dis = 0
        if self.battery_size == 75:
            dis = 260
        elif self.battery_size == 100:
            dis = 315
        
        print(f"This car can go about {dis} miles on a full charge")    
    
    def upgrade_battery(self):
        if self.battery_size!=100:
            self.battery_size  = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")
    

enerNem = ElectricCar('Nem', "nginx", 2022)
enerNem.battery.get_range()
enerNem.battery.upgrade_battery()
enerNem.battery.get_range()