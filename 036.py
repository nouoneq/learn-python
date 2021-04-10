casa = float(input('Qual o valor da casa? '))
salario = float(input('Preciso saber do seu salario para aprovar o financiamento: '))
tempo = int(input('Em quantos anos voce planeja pagar? '))
verf = (casa/tempo)/12
sal = salario*0.30
if verf <= sal:
    print('TEMPO: {}\nMENSALIDADE: R${:.2f}'.format(tempo,verf))
    print('\033[0;32mPARABENS, O FINANCIAMENTO FOI APROVADO!\033[m')

else:
    print('\033[0;31mINFELIZMENTE SEU FINANCIAMENTO NAO FOI APROVADO, TENTE PAGAR EM MAIS TEMPO!\033[m')
