import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            data = json.load(f)
            return data  # Return the loaded JSON data
    except FileNotFoundError:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    username += " "
    filename = 'username.json'
    with open(filename, 'w') as f:  # 'w' mode to overwrite existing data
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    stored_username = get_stored_username()
    if stored_username:
        confirmation = input(f"Is this your username => {stored_username} (y/n): ")
        if confirmation.lower().startswith('y'):
            print(f"Welcome back, {stored_username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"Welcome, {username}!")

greet_user()
