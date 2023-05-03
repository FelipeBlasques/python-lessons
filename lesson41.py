# exercise

name = 'Felipe Blasques'

count = 0
new_name = ''

while count < len(name):
    letter = name[count]
    new_name += f'*{letter}' 
    count += 1

print(new_name)

