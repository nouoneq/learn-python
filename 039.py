# leia a idade de um rapaz e diga quanto tempo falta para o alistamento ou se ta na hora ou se passou do tempo

from datetime import date

ano = int(input('Ano de nascimento: '))
hoje = date.today().year
if hoje-ano < 18:
    c = 18-(hoje-ano)
    print('Voce vai se alistar daqui a {} anos'.format(c))
elif hoje-ano == 18:
    print('ESTA NA HORA DE SE ALISTAR!')
else:
    c = hoje-ano - 18
    print('PASSOU {} anos DO PRAZO DE ALISTAMENTO!'.format(c))
