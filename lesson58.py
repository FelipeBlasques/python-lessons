# start of tuples

names = ['Felipe', 'Navarro', 'Blasques']
name1, name2, name3 = names
print(name2)

_, name2, *_ = ['Felipe', 'Navarro', 'Blasques']
print(name2, _)

