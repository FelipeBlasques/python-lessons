# id/flag

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))
print(id(v2))
print(id(v3))

print(10 * '-')


condition = True
on_the_if = None

if condition:
    on_the_if = True
    print(f'Do it')
else:
    print(f'Dont do it')

print(on_the_if, on_the_if is None)
print(on_the_if, on_the_if is not None)