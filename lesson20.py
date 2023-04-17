# exercise

first_value = input('Type a value: ')
second_value = input('Type other value: ')

if first_value > second_value:
    print(f'{first_value} is major then {second_value}')
elif first_value == second_value:
    print(f'{first_value} is equals then {second_value}')
elif first_value < second_value:
    print(f'{first_value} is minor then {second_value}')
else:
    print(f'error')

