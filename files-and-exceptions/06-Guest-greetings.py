file_name = 'guest_book.txt'

user_details = ""

while not user_details:
    user_details = input("Enter your name: ")

user_details += "\n"  
print(f"Welcome {user_details}")

with open(file_name,'w') as file_obj:
    file_obj.write(user_details)