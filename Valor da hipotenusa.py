import math
ca = int(input('Digite o valor do cateto adjacente: '))
co = int(input('Digite o valor do cateto oposto: '))
c = ca**2 + co**2
h = math.sqrt(c)
print(f'O valor da hipotenusa de acordo com os valores do cateto  é {h}.')
