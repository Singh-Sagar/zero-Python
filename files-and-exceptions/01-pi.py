filename = 'files-and-exceptions/one-million.txt'
with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
counter = 0
for line in lines:
    pi_string += line.strip() # clears any whitespace around the text
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digit of pi!")