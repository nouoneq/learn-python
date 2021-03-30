# leia um número de 4 dígitos de 0 a 9999 e mostre cada um separadamente

n1  = int(input('Digite um número de 4 dígitos: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Analisando o número {} '.format(n1))
print('unidade: {}'.format(u))
print('dezena:  {}'.format(d))
print('centena: {}'.format(c))
print('milhar:  {}'.format(m))

