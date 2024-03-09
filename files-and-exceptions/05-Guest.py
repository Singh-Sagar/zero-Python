
file_name = 'guest_details.txt'

user_name = input("What is your name?: ")
with open(file_name,'w') as file_obj:
    file_obj.write(user_name)
