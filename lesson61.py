# exercise

import os as o

lista = []

while True:
    resp = input(f'What do you want to do? \n [i] to insert\n [d] to delete\n [l] to list\n [e] to exit\n')
    if resp == 'i':
        o.system('clear')
        valor = input(f'What product you want to add? ')
        lista.append(valor)
        o.system('clear')
    elif resp == 'd':
        o.system('clear')
        id = input(f'What is the ID of the product you want to delete? ')
        id = int(id)
        if id > len(lista):
            print('ID doest exist')
        else:
            del lista[id]
            o.system('clear')
    elif resp == 'l':
        o.system('clear')
        print(f'The list in this moment: ')
        for item in enumerate(lista):
            i, name = item
            print(i, name)
        print(f'\n')    
    elif resp == 'e':
        break
    else:
        print('Wrong letter')
    
