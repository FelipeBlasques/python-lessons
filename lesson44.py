# exercise

phrase = 'The Python is a programmer language and Python have be created by Guido'.lower()

i = 0
count = 0
most_appears = ' '
while i < len(phrase):
    letter = phrase[i]
    if letter != ' ':
        how_many_letters = phrase.count(letter)

    if how_many_letters > count:
        count = how_many_letters
        most_appears = letter
    i += 1
print(f'The letter that appears the most is "{most_appears}" and it appears {count} times')
