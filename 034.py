# leia leia o salario e calcule o valor do aumento
# para salarios acima de R$1250.00 aumente 10% e para os inferiores aumente 15%.


sal = float(input('Digite seu salario para calcular o aumento: '))
if sal > 1250:
    amt = (sal*0.10)+sal
    print('SEU SALARIO PASSOU DE R${:.2f} PARA R${:.2f}'.format(sal,amt))
else:
    amt = (sal*0.15)+sal
    print('SEU SALARIO PASSOU DE R${:.2f} PARA R${:.2f}'.format(sal,amt))
