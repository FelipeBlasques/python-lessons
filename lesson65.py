# tuples

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tuplea = 'Python', 'is', 'good'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista
print(p, u, ap)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string)
print(*tuplea)

print(*salas, sep='\n')