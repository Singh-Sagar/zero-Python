import json

filename = 'number.json'

with open(filename) as f:
    x = json.load(f)
    # print(f.read())

print(f"I know your favorite numbers, it's {x}")