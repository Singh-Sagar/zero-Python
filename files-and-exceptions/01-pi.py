filename = 'files-and-exceptions/one-million.txt'
with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
counter = 0
for line in lines:
    pi_string += line.strip() # clears any whitespace around the text
    
print(f"{pi_string[:52]}...")
print(len(pi_string))