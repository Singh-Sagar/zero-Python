# import json

# def save_fav_num():
#     filename = 'fav_num.json'

#     fav_num = input("enter your favorite number: ")
#     with open(filename) as f:
#         json.dump(f,fav_num)
    
#     return filename

# def retrieve_fav_num(file):
#     with open(file,'w') as f:
#         x = json.load(f)
    
#     return x

# while True:
#     file_add = 'fav_num.json'
#     try:
#         with open(file_add,'w') as f:
#             x = json.load(f)
#         print(x)
#     except:
#         file_add = save_fav_num()
#     else:
#         break

import json

def save_fav_num():
    filename = 'fav_num.json'

    fav_num = input("Enter your favorite number: ")
    with open(filename, 'w') as f:  # Open file for writing
        json.dump(fav_num, f)  # Corrected usage of json.dump()
    
    return filename

def retrieve_fav_num(file):
    with open(file, 'r') as f:  # Open file for reading
        x = json.load(f)  # Corrected usage of json.load()
    
    return x

while True:
    file_add = 'fav_num.json'
    try:
        x = retrieve_fav_num(file_add)
        print("Your favorite number is:", x)
    except FileNotFoundError:  # Catch specific exception
        file_add = save_fav_num()
    else:
        break