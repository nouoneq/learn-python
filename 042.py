
m1 = float(input('DIGITE UM LADO: '))
m2 = float(input('DIGITE OUTRO LADO: '))
m3 = float(input('DIGITE O OUTRO LADO: '))
if (m1+m2) > m3 and (m2+m3) > m1 and (m1+m3) > m2:
    print('EH POSSIVEL FORMAR UM TRIANGULO!')
    if m1 == m2 == m3:
        print('TRIANGULO EQUILATERO')
    elif m1 != m2 and m2 != m3 and m1 != m3:
        print('TRIANGULO ESCALENO')
    else:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO EH POSSIVEL FORMAR UM TRIANGULO!')
