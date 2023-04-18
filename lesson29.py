# try/except

number = input('Type a number: ')

try:
    print(f'STR: ', number)
    number = float(number)
    print(f'FLOAT: ', number)
    print(f'The double of {number} is {number * 2}')
except:
    print(f'Is not a number')



