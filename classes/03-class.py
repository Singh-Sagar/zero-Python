
class Users:

    def __init__(self, first_name, last_name,verified,mail):
        self.first_name = first_name
        self.last_name = last_name
        self.verified = verified
        self.mail = mail
    

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}\n{self.verified}\n{self.mail}")
    

    def greet_user(self):
        print(f"Hello {self.first_name}")
    

x = Users("Spike", "spigiel", True, "spike@hotmail.com")
# x.describe_user()
x.greet_user()
user_2 = Users("Faye","Valentine",False, "fayeV.9@yahoo.com")
user_2.greet_user()