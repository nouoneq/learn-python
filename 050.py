# leia 6 numeros insteiros e mostre a soma dos pares.

s = 0
print('VOCE VAI DIGITAR 6 NUMEROS!')
for c in range(1,7):
    num = int(input('n{}: '.format(c)))
    if num % 2 == 0:
        s = num + s
        num = num + s
print('A SOMA DOS NUMEROS PARES: {}'.format(s))
