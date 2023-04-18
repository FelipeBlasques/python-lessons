# exercise

name = input(f'Whats your first name: ')
letters = len(name)

if letters <= 4:
    print(f'Your name has a small size')
elif letters == 5 or letters == 6:
    print(f'Your name has a normal size')
elif letters > 6:
    print(f'Your name has a big size')
else:
    print(f'error')

