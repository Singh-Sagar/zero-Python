file_name = 'describe_your_why.txt'
why = ''

while not why:
    why = input("Why do you like programming?: ")
why += '\n'

with open(file_name,'a') as file_obj:
    file_obj.write(why)