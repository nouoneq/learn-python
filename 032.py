# leia um ano e determine se ele eh bisexto

from datetime import date

ano = int(input('''
DIGITE '0' PARA VERIFICAR O ANO ATUAL!
OU
DIGITE UM ANO: '''))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print('({}) BISSEXTO!'.format(ano))
else:
    if (ano % 4 == 0 and ano % 100 != 0):
        print('({}) BISSEXTO!'.format(ano))
    else:
        print('({}) NAO BISSEXTO!'.format(ano))
