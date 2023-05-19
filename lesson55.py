# list 'RAM'

list_a = ['Felipe', 'Blasques', 1, True, 1.2]
# list_b = list_a --> didnt work like copy
list_b = list_a.copy()

list_a[0] = 'anything'
print(list_a)
print(list_b)