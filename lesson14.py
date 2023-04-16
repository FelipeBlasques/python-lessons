# format

a = 'A'
b = 'B'
c = 1.1
string = 'a={name1}\na={name1}\na={name1}\nb={name2}\nc={name3:.2f}'
format = string.format(
    name1=a, name2=b, name3=c)

print(format)