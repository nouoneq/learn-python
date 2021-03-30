# leia o cateto oposto e o adjacente >> calcule a hipotenusa

import math

opst = float(input('Digite o valor do cateto oposto: '))
adjs = float(input('Digite o valor do cateto adjacente: '))
hipo = math.hypot(opst,adjs)
print('O valor da hipotenusa é: {:.2f}'.format(hipo))