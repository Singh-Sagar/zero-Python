
file_name = 'files-and-exceptions/learning_python.txt'

with open(file_name) as file_obj:
    text_list = file_obj.readlines()

str_text = ''
for i in text_list:
    str_text += i

#print(str_text[:20])
print(str_text.replace('Python', 'C'))
# print(str_text)