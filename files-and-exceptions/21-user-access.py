import json

filename = 'username.json'

with open(filename) as f:
    data = f.read()

user_input = input("What's your name?: ")
if user_input in data:
    print(f"Welcome back {user_input}")