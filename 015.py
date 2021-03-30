# leia a quantidade de dias que um carro foi alugado e quantos KM ele percorreu 
#       R$60 por dia alugado e R$0,15 por KM rodado 

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Nesse tempo, quantos KMs foram rodados? '))
total = (dias*60)+(km*0.15)
print('O total a pagar é de: R${} '.format(total))