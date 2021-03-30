# Leia um número que mostre o dobro o triplo e a raiz quadrada.

n1 = float(input('Digite um número: '))
dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)
print('O dobro de {0} é {1} \nO triplo de {0} é {2} \nA raiz de {0} é {3}'.format(n1,dobro,triplo,raiz))