# randomize um numero entre 0 e 5 e faca um jogo de acerto.

import random

rnd = random.randint(0,5)
usu = int(input('DIGITE UM NUMERO ENTRE 0-5 :'))
if rnd == usu:
	print('VOCE ACERTOU!')
else:
	print('VOCE ERROU, O NUMERO ERA: {}'.format(rnd))