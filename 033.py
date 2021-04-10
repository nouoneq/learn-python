# leia 3 numeros e diga qual eh o maior e o menor.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digiter outro numero: '))
n3 = int(input('Digite mais um numero: '))
if n1>n2 and n1>n3:
    print('MAIOR NUMERO: {}'.format(n1))
elif n2>n1 and n2>n3:
    print('MAIOR NUMERO: {}'.format(n2))
else:
    print('MAIOR NUMERO: {}'.format(n3))

if n1<n2 and n1<n3:
    print('MENOR NUMERO: {}'.format(n1))
elif n2<n1 and n2<n3:
    print('MENOR NUMERO: {}'.format(n2))
else:
    print('MENOR NUMERO: {}'.format(n3))
