# leia a velocidade de um carro, se ele ultrapassou 80Km/h multe ele. R$7 p/ km acima


print('LIMITE DE VELOCIDADE ** 80KM/h **')
carro = int(input('Digite a velocidade do carro: '))
multa = (carro - 80) * 7
if carro >=81:
	print('VOCE ULTRAPASSOU O LIMITE DE VELOCIDADE!')
	print('SUA MULTA EH DE: R${:.2f}'.format(multa))
else :
	print('Lembre-se do limite de velocidade!')
	print('Tenha um um bom passeio!')
