#

for i in range(10):
    if i == 2:
        print('i is 2, jumping...')
        continue
    if i == 8:
        print('i is 8, your else is not running')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('finish the for with sucessfuly!')
    