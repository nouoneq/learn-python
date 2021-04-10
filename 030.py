# leia um numero inteiro e diga se eh par ou impar

print('PAR OU IMPAR? ')
num = int(input('Digite um numero inteiro: '))
if num % 2 == 0:
	print('O NUMERO {} EH PAR!'.format(num))
else:
	print('O NUMERO {} EH IMPAR'.format(num))
