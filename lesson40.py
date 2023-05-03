# while in while

lines = 5
colums = 5

num_lines = 1
while num_lines <= lines:
    num_colums = 1
    while num_colums <= colums:
        print(f'{num_lines=}, {num_colums=}')
        num_colums += 1
    num_lines += 1

print('End')