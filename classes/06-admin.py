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


class Admin:

    def __init__(self,first_name, last_name, verified, mail):
        super().__init__(first_name,last_name,verified, mail)
        self.privileges = ['can add post', ' can delete post', 'can ban user',
                           'can shut down the network']
        
    def show_privileges(self):
        print("PRIVILEGES: ", end = "")
        num = 1
        for i in self.privilages:
            print(num, " " , i)
            num += 1
    
admin1 = Admin("daniel","kaiend",True, "danielK.12@chimp.com")
admin1.show_privilages()