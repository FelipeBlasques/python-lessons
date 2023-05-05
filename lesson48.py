# for

text = 'Felipe'.__iter__()
print(text)

text2 = iter('Felipe')
print(text2.__next__())
print(text2.__next__())
print(text2.__next__())
print(next(text2))
print(next(text2))
print(next(text2))
print('---------------')

# for letter in txt:

txt = 'FelipeBlasques'
iterator = iter(txt)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
