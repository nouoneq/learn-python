# leia o preço de um produto e mostre o valor dele com desconto de 5%.

prod = float(input('Digite o valor do produto: '))
desc = prod*0.05
total = prod-desc
print('O valor do produto é R${:.2f} mas com desconto fica R${:.2f}'.format(prod,total)) 