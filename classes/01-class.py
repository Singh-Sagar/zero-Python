class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def returnAge(self):
        print(self.age)
    
    def woof(self):
        print("woof woof")


pandu = Dog("pandu", 4)
pandu.returnAge()
pandu.woof()