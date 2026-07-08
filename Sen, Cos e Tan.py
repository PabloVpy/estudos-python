import math
n = int(input('Digite o valor do ângulo:'))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print(f'O ângulo {n} tem o valor de sen {sen}, cos {cos} e tan {tan}')
