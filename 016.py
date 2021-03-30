# leia um número real e mostre sua porção inteira.

import math

n1 = float(input('Digite um número real: '))
print('{:.0f}'.format(n1))
print(math.floor(n1))
print(math.trunc(n1))