# exercise

number = input(f'Type a integer number: ')

try:
    number = int(number)
    if number % 2 == 0:
        print(f'the number is even')
    else:
        print(f'the number is odd')
except:
    print(f'the number is not a integer number')