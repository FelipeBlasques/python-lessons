# exercise
import os

WORD = 'love'

start = 'Y'

while start == 'Y':
    os.system('clear')
    count = 0
    SECRET_WORD = ''
    for i in WORD:
        SECRET_WORD += f'*'
    while True:
        count += 1
        if SECRET_WORD == WORD:
                os.system('clear')
                print(f'Great! You win the game!')
                print(f'You try {count-1} times')
                break
        letter = input(f'type a letter: ')
        if len(letter) > 1:
            print('Digite apenas uma letra')
        else:
            for i in range(len(WORD)):
                if letter == WORD[i]:
                    SECRET_WORD = SECRET_WORD[:i] + letter + SECRET_WORD[i+1:]
        print(SECRET_WORD)
                
    start = input(f'Do you want to play again? (Y/N)').upper()
