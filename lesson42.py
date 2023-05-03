# exercise

while True:

    calc = input('Do you want to do a math operation? (Y|N):  ').upper()

    if calc == 'N':
        break

    while calc == 'Y':
        num_1 = float(input('Type a number:  '))
        num_2 = float(input('Type other number:  '))
        res = float()
    
        symbol = input('What type of operation do you want? (| + | - | * | / |):  ')

        if symbol == '+':
            res = num_1 + num_2
            print(f'The result of {num_1} + {num_2} is equal {res}')
            break
        elif symbol == '-':
            res = num_1 - num_2
            print(f'The result of {num_1} - {num_2} is equal {res}')
            break
        elif symbol == '*':
            res = num_1 * num_2
            print(f'The result of {num_1} * {num_2} is equal {res}')
            break
        elif symbol == '/':
            res = num_1 / num_2
            print(f'The result of {num_1} / {num_2} is equal {res}')
            break
        else:
            print('Invallid')
    
    print('Invalid')

     