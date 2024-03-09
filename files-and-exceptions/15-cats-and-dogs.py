dogs_file = 'dogs.txt'
cats_file = 'cats.txt'
try:
    with open(dogs_file) as d_f:
        dogs_text = d_f.read()
    
    with open(cats_file) as c_f:
        cats_text = c_f.read()
except FileNotFoundError:
    print('One of the file does not exist in the mentioned directory')
else:
    print(f"Dogs\n{dogs_text}")
    print()
    print(f"Cats\n{cats_text}")
