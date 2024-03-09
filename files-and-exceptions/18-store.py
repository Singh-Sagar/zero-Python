import json

numbers = [1, 23, 12, 15, 19]

file_name = 'numbers.json'
with open(file_name,'w') as f:
    json.dump(numbers,f)
