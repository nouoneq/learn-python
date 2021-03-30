# leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('Tem o nome "SILVA" ?')
nome = str(input('Digite o nome: ')).strip()
print('Seu nome tem "SILVA" ? {}'.format('SILVA' in nome.upper()))