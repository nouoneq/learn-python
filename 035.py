# leia 3 medidas e diga se eh possivel formar um triangulo

import math

m1 = float(input('DIGITE UMA MEDIDA: '))
m2 = float(input('DIGITE OUTRA MEDIDA: '))
m3 = float(input('DIGITE MAIS UMA MEDIDA: '))
SPC = '='*5
if (m1+m2) > m3 and (m2+m3) > m1 and (m1+m3) > m2:
    print('{0}EH POSSIVEL FORMAR UM TRIANGULO!{0}'.format(SPC))
else:
    print('{0}NAO EH POSSIVEL FORMAR UM TRIANGULO!{0}'.format(SPC))
