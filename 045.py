# jokenpo

from random import randint
from time import sleep

lista = ['PEDRA','PAPEL','TESOURA']
print(lista[0])

esc = int(input('''
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
~$ '''))
rnd = randint(0,2)
print('JO')
sleep(.6)
print('KEN')
sleep(.6)
print('PO!')
sleep(.4)
print('=-'*20)
print('VOCE JOGOU {}\nO PC JOGOU: {}'.format(lista[esc],lista[rnd]))
print('=-'*20)
if esc == rnd:
    print('EMPATE!')
elif esc == 0 and rnd == 1 or esc == 1 and rnd == 2 or esc == 2 and rnd == 0:
    print('PC WIN')
elif esc == 1 and rnd == 0 or esc == 2 and rnd == 1 or esc == 0 and rnd == 2:
    print('YOU WIN')
else:
    print('OPCAO INVALIDA')
