# f string

name = 'Felipe Blasques'
height = 1.73
weight = 85
imc = weight / height ** 2

line = f'{name} has {height:.2f} of height, {weight:.1f} of weight and his IMC is {imc:.2f}'

print(line)

