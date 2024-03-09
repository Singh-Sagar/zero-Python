filename = 'files-and-exceptions/learning_python.txt'

with open(filename) as file_obj:
    text_list = file_obj.readlines()

for i in text_list:
    print(i,end="")
