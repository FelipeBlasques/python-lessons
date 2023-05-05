# for / in

text = 'Python'

new_text = ''
for letter in text:
    new_text += f'*{letter}'
    print(letter)
print(new_text + '*')