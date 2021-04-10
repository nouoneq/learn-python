# soma de todos numeros impares, multiplos de 3 (1 a 500)

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont += 1
print(cont,soma)
