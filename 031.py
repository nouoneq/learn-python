# leia a distancia de uma viagem e calcule o preco da passagem
# R$0.50 km rodado ate 200Km, para viagens mais longas R$0.45

dist = int(input('Digite a distancia da sua viagem: '))
if dist <= 200 :
	tax = 0.50*dist
	print('Sua passagem custou: R${:.2f}'.format(tax))
else:
	tax = 0.45*dist
	print('Sua passagem custou: R${:.2f}'.format(tax))
