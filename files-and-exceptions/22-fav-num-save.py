# import json

# filename = 'number.json'
# x = (input("what is your favorite number? : "))
# with open('filename','w') as f:
#     json.dump(filename,x)

import json

filename = 'number.json'
x = input("what is your favorite number? : ")
with open(filename, 'w') as f:  # Using the variable filename instead of 'filename'
    json.dump(x, f)  # Dumping the value of x to the file
