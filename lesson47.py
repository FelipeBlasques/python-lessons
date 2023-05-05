# exercise - division table (0 - 10)

j = range(1, 10)
for i in j:

    print(f'Divisors of {i}')

    division = range(0, 11, i)
    for divisor in division:
        print(divisor)
 
    print('----------')
