# Leia o nome de uma pessoa e mostre 
#   -> nome com todas as letras maiúsculas;
#   -> nome com todas minúsculas;
#   -> quantas letras tem o nome completo(sem contar com espaços);
#   -> quantas letras tem o primeiro nome.

nome_completo = input('Digite o seu nome: ')
letras_nome = nome_completo.split()
print('Nome completo maiúsculo:            ',nome_completo.upper())
print('Nome completo minúsculo:            ',nome_completo.lower())
print('Nº de letras nome completo:         ',len(nome_completo.replace(' ', '')))
print('Quantidade de letras de {} é:     {}'.format(letras_nome[0],len(letras_nome[0])))
