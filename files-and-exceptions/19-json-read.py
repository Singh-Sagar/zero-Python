import json

filename = 'numbers.json'

with open(filename) as f:
    numbers1 = json.load(f)

print(numbers1)