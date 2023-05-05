# while - else

string = 'anything else'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)
    i += 1
else:
    print('The string doesnt have spaces')
print('Out of while')