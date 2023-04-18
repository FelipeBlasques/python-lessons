# exercise

time = input(f'What time is it? ')

try:
    time = int(time)
    morning = time >= 0 and time <= 11
    afternoon = time >= 12 and time <= 17
    night = time >= 18 and time <= 23

    if morning:
        print(f'Good Morning')
    elif afternoon:
        print(f'Good Afternoon')
    elif night:
        print(f'Good Night')
    else:
        print(f'Its not valid')
except:
    print(f'Its not valid')