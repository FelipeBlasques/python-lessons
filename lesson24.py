# in/not in


# 0 1 2 3 4 5
# F E L I P E
#-6-5-4-3-2-1

name = 'felipe'
print(name[2])
print(name[-4])

print('l' in name)
print('a' in name)
print( 10 * '-')
print('lipe' in name)
print('ary' in name)
print( 10 * '-')
print('lipe' not in name)
print('ary' not in name)

print( 10 * '-')
print( 10 * '-')

name = input('Type your name: ')
search = input('Type a search: ')

if search in name:
    print(f'{search} are in {name}')
else:
    print(f'{search} arent in {name}')
