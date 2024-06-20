my_name = 'open_t.txt'

file = open(my_name, mode = 'r', encoding= 'UTF-8')
file_content = file.read()
file.close()

print(file_content)
