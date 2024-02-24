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


class Admin(Users):

    def __init__(self,first_name, last_name, verified, mail):
        super().__init__(first_name,last_name,verified, mail)
        self.privileges = Privileges(['add users'])

class Privileges:

    def __init__(self, privileges=[] ):
        self.privileges = privileges
    
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")



admin1 = Admin("daniel","kaiend",True, "danielK.12@chimp.com")
admin1.privileges.show_privileges()