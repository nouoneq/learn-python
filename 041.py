from datetime import date

tdy = date.today().year
ano = int(input('Diga o ano que ele nasceu: '))
print('IDADE: {}'.format(tdy-ano))
if tdy-ano <= 9:
    print('CATEGORIA MIRIM')
elif tdy-ano <= 14:
    print('CATEGORIA INFANTIL')
elif tdy-ano <= 19:
    print('CATEGORIA JUNIOR')
elif tdy-ano <= 20:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')
