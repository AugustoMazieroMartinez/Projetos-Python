name = input('Digite seu Nome: ')
name_size = len(name)
new_string = ''
index = 0
while index < name_size:
    new_string += f'*{name[index]}'
    index += 1
print(new_string)