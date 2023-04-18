# CONS/var

speed = int(input(f'Speed of the car: '))
car_local = int(input(f'Local of the car: '))

CHECK_1 = 60
LOCAL_1 = 100
CHECK_RANGE = 1

range_minus = car_local >= (LOCAL_1 - CHECK_RANGE) 
range_plus = car_local <= (LOCAL_1 + CHECK_RANGE)

if range_minus and range_plus:
    if speed <= CHECK_1:
        print(f'on limit')
    else:
        print(f'out of limit')
else:
    print(f'car out of range')