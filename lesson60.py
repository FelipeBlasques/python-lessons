# enumerate 

lista = ['Felipe', 'Navarro', 'Blasques']
lista.append('John')

for i, name in enumerate(lista):
    print(i, name, lista[i])

print('----------')

for item in enumerate(lista):
    i, name = item
    print(i, name)

print('----------')

for tuple_enumerate in enumerate(lista):
    print('FOR of tuple:')
    for valor in tuple_enumerate:
        print(f'\t{valor}')