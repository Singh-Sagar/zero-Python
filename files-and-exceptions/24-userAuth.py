import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            data = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return data

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    username += " "
    filename = 'username.json'
    with open(filename, 'a') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()[0]
    confirmation = input(f"is this your username => {username} (y/n): ")
    if confirmation.lower()[0]=='y':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()