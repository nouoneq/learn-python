# leia dois numeros e diga qual eh o maior e o menor, senao existir um maior diga que sao iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print('{} > {}'.format(n1,n2))
elif n1 < n2:
    print('{} < {}'.format(n1,n2))
else:
    print('Os valores que colocou sao iguais! ({})'.format(n1))
