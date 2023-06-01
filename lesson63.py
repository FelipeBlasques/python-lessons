# split / join

phrase = '   Look   , this guy          '
list_raw = phrase.split(',')

list_fixed = []
for i, phrase in enumerate(list_raw):
    list_fixed.append(list_raw[i].strip())

print(list_raw)
print(list_fixed)

phrase_plus = ', '.join(list_fixed)
print(phrase_plus)