# Exercise

name = input('Whats your name? \n')
age = input('How old are you? \n')

if name and age != False:
    print(f'Your name is {name}')
    print(f'Your inverted name is {name[::-1]}')
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[len(name)-1]}')
    if ' ' in name:
        print(f'Your name has spaces')
    else:
        print(f'Your name has no spaces')
else:
    print(f'Error') 