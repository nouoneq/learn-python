# leia uma frase e mostre quantas vezes aparece a letra "a", e em que posição aparece na primeira vez e na última.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes.'.format(frase.count('A')))
print('Primeira letra "a"  ->>  {}'.format(frase.find('A')+1))
print('Última letra "a"    ->>  {}'.format(frase.rfind('A')+1))
