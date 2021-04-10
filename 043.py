peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))
imc = peso/(altura**2)
print('SEU IMC: {:.2f} '.format(imc), end='')
if imc < 18.5:
    print('VOCE TA ABAIXO DO PESO!')
elif imc > 18.5 and imc < 25:
        print('VOCE TA COM O PESO IDEAL!')
elif imc > 25 and imc < 30:
        print('VOCE TA COM SOBREPESO!')
elif imc > 30 and imc < 40:
        print('VOCE TA COM OBESIDADE!')
else:
    print('VOCE TA COM OBESIDADE MORBIDA!!!!')
