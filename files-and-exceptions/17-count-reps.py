
file_names = ['dorian_grey.txt','tale_of_two_cities.txt','shakespear.txt']

def count_words(filename,word):
    """Count the approximate number of words in a file"""
    try:
        with open(filename,encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        rep = contents.lower().count(word)
        print(f"Word '{word}' is repeated {rep} times")
        print()

for i in file_names:
    count_words(i,'then')