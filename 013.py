# leia o salário de um funcionário e mostre o aumento de 15% em seu salário.

sal = float(input('Qual o salário do funcionário? '))
aumento = sal*0.15
sal_f = sal+aumento
print('O salário do funcionário passou de R${:.2f} para R${:.2f} com o aumento de 15%'.format(sal,sal_f))