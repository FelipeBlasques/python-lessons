#  or

enter = input('[E]nter [L]eave\n')
password = input('Password: ')

right_password = '123'

if (enter == 'E' or enter == 'e') and password == right_password:
    print('Enter')
elif (enter == 'L' or enter == 'l') and password == right_password:
    print('Leave')
else:
    print('Wrong password')