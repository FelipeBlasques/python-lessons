#and

enter = input('[E]nter [L]eave')
password = input('Password: ')

right_password = '123'

if enter == 'E' and password == right_password:
    print('Enter')
elif enter == 'L' and password == right_password:
    print('Leave')
else:
    print('Error')
