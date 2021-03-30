# leia o nome de uma cidade e diga se ela começa com o nome "SANTO"

print('O nome da cidade começa com "Santo" ? ')
cidade = str(input('Digite o nome de uma cidade: ',)).strip()
print(cidade[:6].upper() == 'SANTO')