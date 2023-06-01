# list in list

classrooms = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(classrooms[1][0])
print(classrooms[0][1])
print(classrooms[2][2])

print('-------------------')

for classroom in classrooms:
    print(f'The classroom is {classroom}')
    for student in classroom:
        print(student)